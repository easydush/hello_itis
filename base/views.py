from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from rest_framework import viewsets, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from base.forms import GroupForm, TeacherForm
from base.models import Student, Group, Teacher
from base.serializers import TeacherSerializer, StudentSerializer


def hello(request):
    print(request.path, request.method)
    if request.method == 'GET':
        return HttpResponse(f'bye-bye!')
    students = Student.objects.values_list('name', flat=True)
    students = ', '.join(students)
    return HttpResponse(f'Hello, {students}!')


class MyView(View):
    def get(self, request):
        return HttpResponse("hi, it's class-based")


class TeacherView(View):
    def get(self, request):
        teachers = Teacher.objects.all()

        form = TeacherForm()
        context = {'teachers': teachers, 'form': form}

        return render(request, 'teachers.html', context=context)

    def post(self, request):
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.save()
            form.save_m2m()

            return redirect('/teachers')

    def put(self, request):
        print(request.PUT)
        form = TeacherForm(request.PUT)
        if form.is_valid():
            teacher = Teacher.objects.filter(name=form.cleaned_data.get('name')).first()
            teacher.surname = form.cleaned_data.get('surname')
            teacher.subject = form.cleaned_data.get('subject')
            teacher = form.save(commit=False)
            teacher.save()
            print(teacher)
            form.save_m2m()

            return redirect('/teachers')


def create_group(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = Group.objects.create(**form.cleaned_data)
            return HttpResponse(group)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GroupForm()

    groups = Group.objects.all()
    return render(request, 'hello.html', {'form': form, 'groups': groups})


class TeacherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teachers to be viewed or edited.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.AllowAny]


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

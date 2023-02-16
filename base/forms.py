from django.forms import ModelForm

from base.models import Group, Teacher


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ('title', 'course')


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

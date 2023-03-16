from django.urls import path, include
from rest_framework import routers
from base.views import hello, create_group, TeacherView, TeacherViewSet, CustomAuthToken, StudentViewSet

router = routers.DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('hello', hello, name='hello'),
    path('hi', TeacherView.as_view()),
    path('group', create_group, name='create-group'),
    path('auth/', CustomAuthToken.as_view()),
    path('', include(router.urls)),
]

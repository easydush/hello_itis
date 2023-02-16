from django.urls import path, include
from rest_framework import routers

from base.views import hello, create_group, TeacherView, TeacherViewSet


router = routers.DefaultRouter()
router.register(r'teachers', TeacherViewSet)

urlpatterns = [
    path('hello', hello, name='hello'),
    path('hi', TeacherView.as_view()),
    path('group', create_group, name='create-group'),
    path('', include(router.urls)),
]

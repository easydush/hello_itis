from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from base.models import Teacher, Group


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class TeacherSerializer(ModelSerializer):
    groups = GroupSerializer(many=True)
    is_current_user = SerializerMethodField()

    def get_is_current_user(self, obj):
        return str(obj.name).startswith('I')

    class Meta:
        model = Teacher
        fields = '__all__'

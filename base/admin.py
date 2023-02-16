from django.contrib import admin
from django.contrib.admin import ModelAdmin

from base.models import Group


# Register your models here.
@admin.register(Group)
class GroupAdmin(ModelAdmin):
    list_display = ('title', 'course')

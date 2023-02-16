from django.db import models


# Create your models here.
class Group(models.Model):
    class Course(models.IntegerChoices):
        FIRST = 1
        SECOND = 2
        THIRD = 3
        FOURTH = 4

    title = models.CharField(max_length=40)
    course = models.IntegerField(choices=Course.choices)

    class Meta:
        unique_together = ('title', 'course')

    def __str__(self):
        return self.title


class Teacher(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    subject = models.SlugField(max_length=40)
    email = models.EmailField()
    groups = models.ManyToManyField(Group, related_name='teachers')

    def __str__(self):
        return f'{self.surname} {self.name}'


class TeacherProfile(models.Model):
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    email = models.EmailField()
    tel_number = models.SlugField(max_length=11)


class Student(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    group = models.ForeignKey(Group,
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True,
                              related_name='group_students')

    def __str__(self):
        return f'{self.group.title} | {self.surname} {self.name}'
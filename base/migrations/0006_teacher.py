# Generated by Django 4.1.6 on 2023-02-16 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_student_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groups', models.ManyToManyField(to='base.group')),
            ],
        ),
    ]
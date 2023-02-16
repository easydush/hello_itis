# Generated by Django 4.1.6 on 2023-02-16 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='name',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='subject',
            field=models.SlugField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='surname',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]
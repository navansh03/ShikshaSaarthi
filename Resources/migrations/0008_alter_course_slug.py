# Generated by Django 4.2.6 on 2023-11-01 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resources', '0007_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-01 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resources', '0008_alter_course_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='slug',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-01 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resources', '0012_subject_video_subject'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Video',
        ),
    ]
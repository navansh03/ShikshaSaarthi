# Generated by Django 4.2.6 on 2023-11-01 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resources', '0016_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='subject',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]

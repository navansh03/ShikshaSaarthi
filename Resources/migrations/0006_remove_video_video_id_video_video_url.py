# Generated by Django 4.2.6 on 2023-10-31 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resources', '0005_delete_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_id',
        ),
        migrations.AddField(
            model_name='video',
            name='video_url',
            field=models.CharField(default=0, max_length=150),
        ),
    ]

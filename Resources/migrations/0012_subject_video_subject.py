# Generated by Django 4.2.6 on 2023-11-01 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Resources', '0011_rename_slug_video_slug2_video_video_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resources.course')),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='subject',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Resources.subject'),
        ),
    ]

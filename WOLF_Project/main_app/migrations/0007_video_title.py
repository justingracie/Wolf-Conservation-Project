# Generated by Django 4.0.5 on 2022-06-07 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_video_caption_alter_video_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(default='no title', max_length=125),
        ),
    ]
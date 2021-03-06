# Generated by Django 4.0.5 on 2022-06-07 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_pack_alter_video_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='title',
            new_name='caption',
        ),
        migrations.AddField(
            model_name='pack',
            name='adults',
            field=models.CharField(default=0, max_length=25),
        ),
        migrations.AddField(
            model_name='pack',
            name='founded',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='pack',
            name='name',
            field=models.CharField(default='unassigned', max_length=125),
        ),
        migrations.AddField(
            model_name='pack',
            name='pups',
            field=models.CharField(default=0, max_length=25),
        ),
        migrations.AddField(
            model_name='pack',
            name='total',
            field=models.CharField(default=0, max_length=25),
        ),
    ]

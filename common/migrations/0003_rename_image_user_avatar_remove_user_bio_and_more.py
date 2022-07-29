# Generated by Django 4.0.6 on 2022-07-29 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_user_bio_user_birthday_user_gender_user_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='image',
            new_name='avatar',
        ),
        migrations.RemoveField(
            model_name='user',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='user',
            name='website',
        ),
        migrations.AddField(
            model_name='user',
            name='job_location',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]

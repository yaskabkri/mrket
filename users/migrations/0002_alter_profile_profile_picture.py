# Generated by Django 5.0.1 on 2024-02-04 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default_profile_picture.jpg', null=True, upload_to='profile_pictures/'),
        ),
    ]
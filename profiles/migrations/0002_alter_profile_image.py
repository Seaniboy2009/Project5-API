# Generated by Django 3.2.18 on 2023-03-26 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='https://res.cloudinary.com/dgj9rjuka/image/upload/v1679853612/Project%205%20API/default_profile_o21i6o_tvkkll.jpg', upload_to='Project 5 API/'),
        ),
    ]
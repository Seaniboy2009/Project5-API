# Generated by Django 3.2.18 on 2023-03-27 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../media/images/default_profile_o21i6o_h3tqjf', upload_to='images/'),
        ),
    ]

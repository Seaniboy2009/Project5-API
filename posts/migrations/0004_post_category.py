# Generated by Django 3.2.18 on 2023-04-19 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='Other', max_length=255),
        ),
    ]
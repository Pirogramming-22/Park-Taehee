# Generated by Django 5.1.5 on 2025-01-20 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_posts_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='likes',
        ),
        migrations.AddField(
            model_name='posts',
            name='dislike',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='posts',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]

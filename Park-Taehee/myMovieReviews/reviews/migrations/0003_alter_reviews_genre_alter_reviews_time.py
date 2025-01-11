# Generated by Django 5.1.4 on 2025-01-10 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_rename_review_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='genre',
            field=models.CharField(choices=[('Action', 'Action'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Horror', 'Horror'), ('Romance', 'Romance'), ('Thriller', 'Thriller'), ('SF', 'SF'), ('Sports', 'Sports'), ('Fantasy', 'Fantasy')], max_length=10),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='time',
            field=models.DurationField(),
        ),
    ]

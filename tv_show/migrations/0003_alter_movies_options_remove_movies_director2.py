# Generated by Django 5.1.4 on 2025-01-06 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tv_show', '0002_movies_director2'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movies',
            options={'verbose_name': 'фильм', 'verbose_name_plural': 'список фильмов'},
        ),
        migrations.RemoveField(
            model_name='movies',
            name='director2',
        ),
    ]

# Generated by Django 2.0.2 on 2020-04-21 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20180404_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='genres',
            field=models.ManyToManyField(blank=True, to='movie.Genres', verbose_name='标签'),
        ),
    ]

# Generated by Django 5.1 on 2024-09-20 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='number_of_views',
            field=models.PositiveIntegerField(default=0, verbose_name='количество просмотров'),
        ),
    ]

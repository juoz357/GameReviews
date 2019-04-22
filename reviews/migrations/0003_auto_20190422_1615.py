# Generated by Django 2.2 on 2019-04-22 13:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20190422_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='review',
            name='game_score',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]

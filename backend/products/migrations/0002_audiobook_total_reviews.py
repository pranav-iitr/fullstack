# Generated by Django 5.0.2 on 2024-07-22 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiobook',
            name='total_reviews',
            field=models.IntegerField(default=0),
        ),
    ]
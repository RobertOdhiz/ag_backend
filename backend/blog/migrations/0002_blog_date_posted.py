# Generated by Django 4.2.5 on 2023-09-17 20:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

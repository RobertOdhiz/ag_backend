# Generated by Django 4.2.5 on 2023-09-17 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-17 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myghala', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Soko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commodity', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='images/')),
                ('ghala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myghala.myghala')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
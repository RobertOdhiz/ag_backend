# Generated by Django 4.2.5 on 2023-09-17 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soko', '0004_remove_soko_ghala_soko_ghala'),
        ('mysoko', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mysoko',
            name='soko',
        ),
        migrations.AlterField(
            model_name='mysoko',
            name='commodity_sold',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soko.soko'),
        ),
    ]

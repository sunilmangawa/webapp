# Generated by Django 4.1.7 on 2023-04-02 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milldata', '0008_device_galla_vibrator_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='milldata',
            name='galla_clear_time',
            field=models.IntegerField(default=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='milldata',
            name='initial_hold',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
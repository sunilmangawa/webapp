# Generated by Django 4.1.7 on 2023-03-17 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milldata', '0005_remove_milldata_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milldata',
            name='katta_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
# Generated by Django 4.1.7 on 2023-03-17 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milldata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='contract_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='contract_start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='actual_hold',
            field=models.IntegerField(default=900),
        ),
        migrations.AddField(
            model_name='device',
            name='circle',
            field=models.IntegerField(default=21),
        ),
        migrations.AddField(
            model_name='device',
            name='circle_hold',
            field=models.IntegerField(default=15),
        ),
        migrations.AddField(
            model_name='device',
            name='feed_hold_time',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='device',
            name='feed_time',
            field=models.IntegerField(default=6),
        ),
        migrations.AddField(
            model_name='device',
            name='initial_hold',
            field=models.IntegerField(default=600),
        ),
        migrations.AddField(
            model_name='device',
            name='ip_address',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='mac_address',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='overload_hold',
            field=models.IntegerField(default=2100),
        ),
        migrations.AddField(
            model_name='device',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=20),
        ),
        migrations.AddField(
            model_name='milldata',
            name='actual_hold',
            field=models.IntegerField(default=900),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='milldata',
            name='circle',
            field=models.IntegerField(default=21),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='milldata',
            name='circle_hold',
            field=models.IntegerField(default=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='milldata',
            name='feed_hold_time',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='milldata',
            name='feed_time',
            field=models.IntegerField(default=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='milldata',
            name='initial_hold',
            field=models.IntegerField(default=600),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='milldata',
            name='overload_hold',
            field=models.IntegerField(default=2100),
            preserve_default=False,
        ),
    ]

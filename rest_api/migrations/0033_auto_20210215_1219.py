# Generated by Django 3.1.3 on 2021-02-15 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0032_auto_20210215_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='creation_status',
            field=models.CharField(choices=[('empty', 'Empty'), ('loading_gtfs', 'Loading GTFS'), ('from_gtfs', 'From GTFS')], default='empty', max_length=20),
        ),
    ]

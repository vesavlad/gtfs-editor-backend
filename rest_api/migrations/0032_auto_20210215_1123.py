# Generated by Django 3.1.3 on 2021-02-15 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0031_auto_20210215_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='loading_gtfs_error_message',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-20 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0019_project_gtfs_creation_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='gtfs_creation_duration',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
# Generated by Django 3.0.7 on 2020-11-10 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_auto_20201102_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fareattribute',
            name='transfers',
            field=models.IntegerField(null=True),
        ),
    ]

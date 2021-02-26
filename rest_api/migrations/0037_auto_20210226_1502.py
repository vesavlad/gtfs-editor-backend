# Generated by Django 3.1.3 on 2021-02-26 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0036_auto_20210226_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fareattribute',
            name='agency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.agency'),
        ),
        migrations.AlterField(
            model_name='farerule',
            name='fare_attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.fareattribute'),
        ),
        migrations.AlterField(
            model_name='frequency',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.trip'),
        ),
        migrations.AlterField(
            model_name='pathway',
            name='from_stop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stop_from', to='rest_api.stop'),
        ),
        migrations.AlterField(
            model_name='pathway',
            name='to_stop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stop_to', to='rest_api.stop'),
        ),
        migrations.AlterField(
            model_name='route',
            name='agency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.agency'),
        ),
        migrations.AlterField(
            model_name='stoptime',
            name='stop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.stop'),
        ),
        migrations.AlterField(
            model_name='stoptime',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stop_times', to='rest_api.trip'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='from_stop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_stop', to='rest_api.stop'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='to_stop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_stop', to='rest_api.stop'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.route'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='shape',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rest_api.shape'),
        ),
    ]

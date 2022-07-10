# Generated by Django 3.0.7 on 2020-10-01 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_id', models.CharField(max_length=50)),
                ('agency_name', models.CharField(max_length=50)),
                ('agency_url', models.URLField()),
                ('agency_timezone', models.CharField(max_length=20)),
                ('agency_lang', models.CharField(max_length=10, null=True)),
                ('agency_phone', models.CharField(max_length=20, null=True)),
                ('agency_fare_url', models.URLField(max_length=255, null=True)),
                ('agency_email', models.EmailField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FareAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fare_id', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('currency_type', models.CharField(max_length=10)),
                ('payment_method', models.IntegerField()),
                ('transfers', models.IntegerField()),
                ('transfer_duration', models.IntegerField()),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest_api.Agency')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_id', models.CharField(max_length=50)),
                ('level_index', models.FloatField()),
                ('level_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_id', models.CharField(max_length=50, null=True)),
                ('route_short_name', models.CharField(max_length=50, null=True)),
                ('route_long_name', models.CharField(max_length=200, null=True)),
                ('route_desc', models.CharField(max_length=50, null=True)),
                ('route_type', models.IntegerField()),
                ('route_url', models.URLField(null=True)),
                ('route_color', models.CharField(max_length=10, null=True)),
                ('route_text_color', models.CharField(max_length=10, null=True)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest_api.Agency')),
            ],
            options={
                'unique_together': {('agency', 'route_id')},
            },
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape_id', models.CharField(max_length=50)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest_api.Project')),
            ],
            options={
                'unique_together': {('project', 'shape_id')},
            },
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop_id', models.CharField(max_length=50)),
                ('stop_code', models.CharField(max_length=50, null=True)),
                ('stop_name', models.CharField(max_length=200)),
                ('stop_lat', models.FloatField()),
                ('stop_lon', models.FloatField()),
                ('stop_url', models.URLField(null=True)),
                ('stop_desc', models.CharField(max_length=200, null=True)),
                ('zone_id', models.CharField(max_length=50, null=True)),
                ('location_type', models.IntegerField(null=True)),
                ('stop_timezone', models.CharField(max_length=200, null=True)),
                ('wheelchair_boarding', models.CharField(max_length=200, null=True)),
                ('platform_code', models.CharField(max_length=200, null=True)),
                ('level_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rest_api.Level')),
                ('parent_station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rest_api.Stop')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest_api.Project')),
            ],
            options={
                'unique_together': {('project', 'stop_id')},
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_id', models.CharField(max_length=50)),
                ('service_id', models.CharField(max_length=50)),
                ('trip_headsign', models.CharField(max_length=100, null=True)),
                ('direction_id', models.CharField(max_length=50, null=True)),
                ('trip_short_name', models.CharField(max_length=50, null=True)),
                ('block_id', models.CharField(max_length=50, null=True)),
                ('wheelchair_accessible', models.IntegerField(null=True)),
                ('bikes_allowed', models.IntegerField(null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest_api.Project')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest_api.Route')),
                ('shape', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='rest_api.Shape')),
            ],
            options={
                'unique_together': {('project', 'trip_id')},
            },
        ),
        migrations.CreateModel(
            name='PublishingURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest_api.Project')),
            ],
            options={
                'unique_together': {('project', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('message', models.CharField(max_length=200)),
                ('publishing_location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest_api.PublishingURL')),
            ],
        ),
        migrations.AddField(
            model_name='level',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest_api.Project'),
        ),
        migrations.CreateModel(
            name='FeedInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_publisher_name', models.CharField(max_length=50)),
                ('feed_publisher_url', models.URLField()),
                ('feed_lang', models.CharField(max_length=10, null=True)),
                ('feed_start_date', models.DateField(null=True)),
                ('feed_end_date', models.DateField(null=True)),
                ('feed_version', models.CharField(max_length=50, null=True)),
                ('feed_id', models.CharField(max_length=50)),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='rest_api.Project')),
            ],
        ),
        migrations.CreateModel(
            name='FareRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fare_attribute', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest_api.FareAttribute')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest_api.Route')),
            ],
        ),
        migrations.AddField(
            model_name='fareattribute',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest_api.Project'),
        ),
        migrations.AddField(
            model_name='agency',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest_api.Project'),
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('from_stop', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='from_stop', to='rest_api.Stop')),
                ('to_stop', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='to_stop', to='rest_api.Stop')),
            ],
            options={
                'unique_together': {('from_stop', 'to_stop')},
            },
        ),
        migrations.CreateModel(
            name='StopTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop_sequence', models.IntegerField()),
                ('arrival_time', models.TimeField(null=True)),
                ('departure_time', models.TimeField(null=True)),
                ('stop_headsign', models.CharField(max_length=50, null=True)),
                ('pickup_type', models.IntegerField(null=True)),
                ('drop_off_type', models.IntegerField(null=True)),
                ('continuous_pickup', models.IntegerField(null=True)),
                ('continuous_drop_off', models.IntegerField(null=True)),
                ('shape_dist_traveled', models.FloatField(null=True)),
                ('timepoint', models.IntegerField(null=True)),
                ('stop', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest_api.Stop')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest_api.Trip')),
            ],
            options={
                'unique_together': {('trip', 'stop', 'stop_sequence')},
            },
        ),
        migrations.CreateModel(
            name='ShapePoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape_pt_sequence', models.IntegerField()),
                ('shape_pt_lat', models.FloatField()),
                ('shape_pt_lon', models.FloatField()),
                ('shape', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points', to='rest_api.Shape')),
            ],
            options={
                'unique_together': {('shape', 'shape_pt_sequence')},
            },
        ),
        migrations.CreateModel(
            name='Pathway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pathway_id', models.CharField(max_length=50)),
                ('pathway_mode', models.IntegerField()),
                ('is_bidirectional', models.BooleanField()),
                ('from_stop', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='stop_from', to='rest_api.Stop')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest_api.Project')),
                ('to_stop', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='stop_to', to='rest_api.Stop')),
            ],
            options={
                'unique_together': {('project', 'pathway_id')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='level',
            unique_together={('project', 'level_id', 'level_index')},
        ),
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('headway_secs', models.PositiveIntegerField()),
                ('exact_times', models.IntegerField()),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest_api.Trip')),
            ],
            options={
                'unique_together': {('trip', 'start_time')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='fareattribute',
            unique_together={('project', 'fare_id')},
        ),
        migrations.CreateModel(
            name='CalendarDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('exception_type', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest_api.Project')),
            ],
            options={
                'unique_together': {('project', 'service_id', 'date')},
            },
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.CharField(max_length=50)),
                ('monday', models.BooleanField()),
                ('tuesday', models.BooleanField()),
                ('wednesday', models.BooleanField()),
                ('thursday', models.BooleanField()),
                ('friday', models.BooleanField()),
                ('saturday', models.BooleanField()),
                ('sunday', models.BooleanField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest_api.Project')),
            ],
            options={
                'unique_together': {('project', 'service_id')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='agency',
            unique_together={('project', 'agency_id')},
        ),
    ]

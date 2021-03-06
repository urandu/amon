# Generated by Django 2.0.2 on 2018-02-19 21:01

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('type', models.CharField(choices=[('metric', 'metric'), ('check', 'check')], default='metric', max_length=10)),
                ('tags', django.contrib.postgres.fields.jsonb.JSONField()),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='MetricData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField()),
                ('value', models.FloatField()),
                ('metric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metrics.Metric')),
            ],
        ),
        migrations.CreateModel(
            name='MetricDataChecks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField()),
                ('value', models.CharField(choices=[('ok', 'ok'), ('warn', 'warn'), ('crit', 'crit'), ('unknown', 'unknown')], default='unknown', max_length=10)),
                ('message', models.TextField()),
                ('metric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metrics.Metric')),
            ],
        ),
        migrations.AlterIndexTogether(
            name='metricdatachecks',
            index_together={('metric', 'timestamp')},
        ),
        migrations.AlterIndexTogether(
            name='metricdata',
            index_together={('metric', 'timestamp')},
        ),
        migrations.AlterUniqueTogether(
            name='metric',
            unique_together={('name', 'tags', 'organization')},
        ),
    ]

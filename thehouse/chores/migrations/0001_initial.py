# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thehouse', '__first__'),
        ('roommate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chore',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('priority', models.CharField(choices=[('low', 'Low'), ('med', 'Medium'), ('high', 'High')], max_length=10)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField()),
                ('date_due', models.DateTimeField()),
                ('repeated', models.BooleanField(default=True)),
                ('repeat_period', models.DurationField()),
                ('assignee', models.ForeignKey(null=True, to='roommate.Roommate')),
                ('house', models.ForeignKey(to='thehouse.House')),
            ],
        ),
    ]

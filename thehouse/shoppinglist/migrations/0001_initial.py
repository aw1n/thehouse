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
            name='ShoppingItem',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('description', models.TextField()),
                ('priority', models.CharField(choices=[('low', 'Low'), ('med', 'Medium'), ('high', 'High')], max_length=10)),
                ('date_created', models.DateTimeField()),
                ('created_by', models.ForeignKey(to='roommate.Roommate')),
                ('house', models.ForeignKey(to='thehouse.House')),
            ],
        ),
    ]

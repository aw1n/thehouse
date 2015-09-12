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
            name='DebtItem',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('paid', models.BooleanField(default=False)),
                ('amount', models.DecimalField(max_digits=6, decimal_places=2)),
                ('date_paid', models.DateTimeField()),
                ('debtor', models.ForeignKey(to='roommate.Roommate')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('totalAmount', models.DecimalField(max_digits=6, decimal_places=2)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField()),
                ('house', models.ForeignKey(to='thehouse.House')),
                ('payer', models.ForeignKey(to='roommate.Roommate')),
            ],
        ),
    ]

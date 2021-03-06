# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 08:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0007_auto_20160125_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='transaction_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 25, 8, 42, 12, 660221)),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='wallet2user_details',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='wallet_debit_record2wallet_credit_record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.Wallet'),
        ),
    ]

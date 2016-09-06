# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-15 04:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('summer_plans', '0010_remove_planrecord_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lottery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.IntegerField(default=0, editable=False)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summer_plans.User')),
            ],
        ),
        migrations.CreateModel(
            name='LotteryList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u540d\u79f0')),
                ('is_on', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5f00\u542f')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summer_plans.PlanCategory')),
                ('lottery', models.ManyToManyField(blank=True, to='summer_plans.Lottery')),
            ],
        ),
    ]
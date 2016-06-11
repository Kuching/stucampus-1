# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-09 17:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000, verbose_name='\u5185\u5bb9')),
                ('thought', models.CharField(blank=True, max_length=1000, null=True, verbose_name='\u611f\u609f')),
                ('like_count', models.IntegerField(default=0, editable=False)),
                ('deleted', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlanCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='\u5206\u7c7b\u540d')),
                ('english_name', models.CharField(max_length=20, unique=True)),
                ('is_on', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5f00\u542f')),
                ('tip_time', models.DateField(blank=True, null=True, verbose_name='\u5f00\u542f\u611f\u609f\u7559\u8a00\u7684\u65f6\u95f4')),
            ],
            options={
                'permissions': (('send_email', '\u53d1\u9001\u90ae\u4ef6'),),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('szu_no', models.CharField(max_length=10, unique=True)),
                ('szu_name', models.CharField(max_length=30)),
                ('szu_ic', models.CharField(max_length=6)),
                ('szu_org_name', models.CharField(max_length=50, null=True)),
                ('szu_sex', models.CharField(max_length=4, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='plan',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='summer_plans.User'),
        ),
        migrations.AddField(
            model_name='plan',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summer_plans.PlanCategory'),
        ),
        migrations.AddField(
            model_name='plan',
            name='like_persons',
            field=models.ManyToManyField(blank=True, related_name='like_persons', to='summer_plans.User'),
        ),
    ]
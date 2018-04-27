# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-26 22:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoopfinder', '0005_auto_20180426_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('reviewed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reviews', to='hoopfinder.User')),
            ],
        ),
    ]

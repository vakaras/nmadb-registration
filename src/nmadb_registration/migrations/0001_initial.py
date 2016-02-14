# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-14 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_db_utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postal_code', django_db_utils.models.PostalNumberField(help_text='Can be looked up in www.post.lt.', max_length=5, verbose_name='postal code')),
                ('living_area', models.CharField(help_text='For example, Vilnius or Smilgių kaimas', max_length=128, verbose_name='living area')),
                ('street', models.CharField(help_text='Street name. For example, A. Vivulskio.', max_length=128, verbose_name='street')),
                ('house_number', models.PositiveSmallIntegerField(verbose_name='house number')),
                ('house_letter', models.CharField(blank=True, help_text='For example, B.', max_length=2, null=True, verbose_name='house letter')),
                ('flat_number', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='flat number')),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True, verbose_name='name')),
                ('result', models.NullBooleanField(help_text='If null, then evaluates expression.', verbose_name='result')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('expression', models.TextField(help_text='When this Python expression evaluates to True, function specified in action is called.', verbose_name='expression')),
            ],
            options={
                'verbose_name': 'condition',
                'ordering': ['name'],
                'verbose_name_plural': 'conditions',
            },
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('town', models.CharField(max_length=45, verbose_name='town')),
                ('municipality_type', models.CharField(blank=True, choices=[('T', 'town'), ('D', 'district')], max_length=2, verbose_name='type')),
                ('code', models.PositiveSmallIntegerField(verbose_name='code')),
            ],
            options={
                'verbose_name': 'municipality',
                'ordering': ['town', 'municipality_type'],
                'verbose_name_plural': 'municipalities',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, unique=True, verbose_name='title')),
            ],
            options={
                'verbose_name': 'school',
                'ordering': ['title'],
                'verbose_name_plural': 'schools',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45, unique=True, verbose_name='title')),
            ],
            options={
                'verbose_name': 'section',
                'ordering': ['title'],
                'verbose_name_plural': 'sections',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='municipality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nmadb_registration.Municipality', verbose_name='municipality'),
        ),
    ]

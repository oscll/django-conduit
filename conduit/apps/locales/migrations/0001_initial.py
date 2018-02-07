# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-31 03:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0003_profile_favorites'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('body', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='profiles.Profile')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=25)),
                ('telefono', models.CharField(max_length=25)),
                ('direccion', models.CharField(max_length=55)),
                ('poblacion', models.CharField(max_length=25)),
                ('provincia', models.CharField(max_length=25)),
                ('latitud', models.CharField(max_length=255)),
                ('longitud', models.CharField(max_length=255)),
                ('foto', models.CharField(blank=True, max_length=255)),
                ('categoria', models.CharField(max_length=25)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locales', to='profiles.Profile')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=30)),
                ('foto', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto', to='locales.Local')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='locales.Local'),
        ),
    ]
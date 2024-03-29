# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-19 03:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Giveaway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_name', models.CharField(max_length=55)),
                ('entries', models.IntegerField(default=5)),
                ('created', models.DateField(default=django.utils.timezone.now)),
                ('updated', models.DateField(default=django.utils.timezone.now)),
                ('image', models.ImageField(null=True, upload_to='giveaways/Img/')),
                ('description', models.TextField()),
                ('price', models.IntegerField(default=2000)),
                ('ending_time', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='GiveawayEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateField(default=django.utils.timezone.now)),
                ('updated', models.DateField(default=django.utils.timezone.now)),
                ('total_points', models.IntegerField()),
                ('facebook_share_count', models.IntegerField(default=0)),
                ('twitter_share_count', models.IntegerField(default=0)),
                ('google_plus_share_count', models.IntegerField(default=0)),
                ('stumble_share_count', models.IntegerField(default=0)),
                ('linked_share_count', models.IntegerField(default=0)),
                ('giveaway', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Giveaway')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=100)),
                ('main_image', models.ImageField(null=True, upload_to='Products/')),
                ('screenshot2', models.ImageField(null=True, upload_to='products/')),
                ('screenshot3', models.ImageField(null=True, upload_to='products/')),
                ('created', models.DateField(default=django.utils.timezone.now, null=True)),
                ('updated', models.DateField(default=django.utils.timezone.now, null=True)),
                ('actual_price', models.IntegerField(default=2000)),
                ('quantity', models.IntegerField(default=5)),
                ('product_file', models.FileField(upload_to='doc_files')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='giveaway',
            name='p_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
        migrations.AddField(
            model_name='giveaway',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

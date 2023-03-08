# Generated by Django 4.1.7 on 2023-03-07 22:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vitrine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreFront',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.ImageField(blank=True, upload_to='')),
                ('name', models.TextField(max_length=30)),
                ('logo', models.ImageField(blank=True, upload_to='')),
                ('theme', models.TextField(max_length=10)),
                ('description', models.TextField(max_length=100)),
                ('is_schedulable', models.BooleanField(default=True)),
                ('address_text', models.TextField(max_length=100)),
                ('address_CEP', models.TextField(max_length=8)),
                ('phone', models.TextField(max_length=11)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('facebook', models.TextField(blank=True, max_length=30)),
                ('instagram', models.TextField(blank=True, max_length=30)),
                ('youtube', models.TextField(blank=True, max_length=30)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration_time', models.TimeField()),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vitrine.storefront')),
            ],
        ),
    ]
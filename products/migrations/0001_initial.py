# Generated by Django 4.1.2 on 2022-10-15 06:30

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='products')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='cover_image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('currency', models.CharField(default='usd', max_length=20)),
                ('info', models.CharField(blank=True, max_length=255, null=True)),
                ('short_description', models.TextField(blank=True, max_length=200, null=True)),
                ('full_description', models.TextField(blank=True, max_length=500, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
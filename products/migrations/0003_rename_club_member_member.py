# Generated by Django 5.0.1 on 2024-11-10 22:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_club_member'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Club_Member',
            new_name='Member',
        ),
    ]
# Generated by Django 3.2 on 2021-05-01 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210501_0152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='user',
        ),
    ]
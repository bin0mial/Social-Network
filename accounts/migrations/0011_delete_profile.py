# Generated by Django 3.2 on 2021-05-02 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
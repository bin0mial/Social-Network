# Generated by Django 3.2 on 2021-05-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='redirect_to',
            field=models.TextField(max_length=255, null=True),
        ),
    ]

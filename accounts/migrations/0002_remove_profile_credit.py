# Generated by Django 2.2.1 on 2019-06-19 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='credit',
        ),
    ]

# Generated by Django 3.0.3 on 2020-09-02 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0019_auto_20200902_0545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='panel',
        ),
    ]
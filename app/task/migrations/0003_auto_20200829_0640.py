# Generated by Django 3.0.3 on 2020-08-29 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20200829_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='status',
            field=models.IntegerField(choices=[(1, 'Wating'), (2, 'Under Process'), (3, 'Done'), (4, 'Total')], default=1),
        ),
    ]

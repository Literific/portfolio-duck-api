# Generated by Django 3.2.6 on 2021-08-29 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20210829_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='brokerage',
            name='opened_at',
            field=models.DateField(default='2020-01-01'),
        ),
    ]
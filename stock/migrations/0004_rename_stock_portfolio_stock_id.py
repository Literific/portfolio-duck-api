# Generated by Django 3.2.6 on 2021-08-29 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_brokerage_opened_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='stock',
            new_name='stock_id',
        ),
    ]
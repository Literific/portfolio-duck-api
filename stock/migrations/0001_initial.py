# Generated by Django 3.2.6 on 2021-08-24 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brokerage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('fidelity', 'Fidelity'), ('etrade', 'Etrade'), ('robinhood', 'Robinhood'), ('vanguard', 'Vanguard'), ('chase', 'Chase'), ('others', 'Others')], default='fidelity', max_length=200)),
            ],
            options={
                'db_table': 'Brokerage',
            },
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Industry',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_id', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('date_slug', models.SlugField(max_length=250)),
                ('open', models.FloatField()),
                ('close', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('volume', models.FloatField()),
                ('twentydayavg', models.FloatField()),
                ('rsi', models.FloatField()),
                ('lstm', models.FloatField()),
                ('industry', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='stock.industry')),
            ],
            options={
                'db_table': 'Stock',
                'ordering': ('-date',),
            },
        ),
    ]

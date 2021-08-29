# Generated by Django 3.2.6 on 2021-08-29 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brokerage',
            name='name',
            field=models.CharField(choices=[('fidelity', 'Fidelity'), ('etrade', 'Etrade'), ('robinhood', 'Robinhood'), ('vanguard', 'Vanguard'), ('chase', 'Chase'), ('others', 'Others')], default='others', max_length=200),
        ),
        migrations.AlterField(
            model_name='industry',
            name='name',
            field=models.CharField(choices=[('technology', 'Technology'), ('consumer', 'Consumer'), ('health', 'Health')], default='technology', max_length=200),
        ),
        migrations.AlterField(
            model_name='stock',
            name='industry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Stock', to='stock.industry'),
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_shares', models.FloatField()),
                ('avg_cost_of_shares', models.FloatField()),
                ('date_updated', models.DateField()),
                ('brokerage', models.ForeignKey(default='others', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='Portfolio', to='stock.brokerage')),
                ('stock', models.ForeignKey(default='cash', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='Portfolio', to='stock.stock')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Portfolio', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Portfolio',
            },
        ),
    ]
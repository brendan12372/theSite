# Generated by Django 4.0.2 on 2022-03-07 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0016_stock_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='floatShares',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='dividendRate',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='dividendYield',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='revenueGrowth',
            field=models.FloatField(blank=True, default=0),
        ),
    ]

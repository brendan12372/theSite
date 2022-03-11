# Generated by Django 4.0.2 on 2022-03-07 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0017_stock_floatshares_alter_stock_dividendrate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='grossProfit',
            field=models.FileField(blank=True, default=0, null=0, upload_to=''),
        ),
        migrations.AddField(
            model_name='stock',
            name='priceToSalesTrailing12Months',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='totalCash',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='totalDebt',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

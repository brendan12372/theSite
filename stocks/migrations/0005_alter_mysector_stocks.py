# Generated by Django 4.0.2 on 2022-03-01 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0004_remove_stock_xxx_mysector_stocks_alter_mysector_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysector',
            name='stocks',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.stock'),
        ),
    ]

# Generated by Django 4.0.2 on 2022-03-07 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0021_remove_stock_response_alter_stock_averagevolume_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='sharesPercentSharesOut',
            field=models.FloatField(default=0, null=True),
        ),
    ]
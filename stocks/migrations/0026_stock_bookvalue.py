# Generated by Django 4.0.2 on 2022-03-13 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0025_stock_grossmargins_stock_grossprofits_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='bookValue',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

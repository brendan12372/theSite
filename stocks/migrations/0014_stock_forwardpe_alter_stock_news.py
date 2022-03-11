# Generated by Django 4.0.2 on 2022-03-07 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0013_alter_stock_averagevolume_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='forwardPE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='news',
            field=models.TextField(blank=True, default=''),
        ),
    ]

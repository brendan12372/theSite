# Generated by Django 4.0.2 on 2022-03-14 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topTen', '0009_stock_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='news',
            field=models.JSONField(blank=True, default={'age': 36, 'country': 'Norway', 'name': 'John'}),
        ),
    ]
# Generated by Django 4.0.2 on 2022-03-13 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0029_rename_feps_stock_pricetobook_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='totalAssets',
        ),
    ]

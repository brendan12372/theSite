# Generated by Django 4.0.2 on 2022-03-02 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0009_alter_stock_xsectorx'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='xsectorx',
        ),
        migrations.AddField(
            model_name='mysector',
            name='ave',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]

# Generated by Django 4.0.2 on 2022-03-01 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_mysector'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='xxx',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stocks.mysector'),
        ),
    ]

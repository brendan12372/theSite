# Generated by Django 4.0.2 on 2022-03-01 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0005_alter_mysector_stocks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mysector',
            name='stocks',
        ),
        migrations.AddField(
            model_name='stock',
            name='xsectorx',
            field=models.ForeignKey(default='Technology', on_delete=django.db.models.deletion.CASCADE, to='stocks.mysector', to_field='name'),
        ),
    ]

# Generated by Django 4.0.2 on 2022-03-03 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topTen', '0003_options_normalize'),
    ]

    operations = [
        migrations.AddField(
            model_name='options',
            name='dir',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

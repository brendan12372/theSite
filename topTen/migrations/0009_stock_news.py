# Generated by Django 4.0.2 on 2022-03-14 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topTen', '0008_alter_sectoroptions_dir_alter_sectoroptions_sortby'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='news',
            field=models.JSONField(blank=True, default={'test': '123'}),
        ),
    ]
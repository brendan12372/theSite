# Generated by Django 4.0.2 on 2022-02-28 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topTen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(blank=True, max_length=200)),
                ('sortBy', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
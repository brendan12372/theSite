# Generated by Django 4.0.2 on 2022-03-07 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0022_alter_stock_sharespercentsharesout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='averageVolume',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='averageVolume10days',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='currentPrice',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='enterpriseToEbitda',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='enterpriseToRevenue',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='enterpriseValue',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='fiftyDayAverage',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='fiftyTwoWeekHigh',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='fiftyTwoWeekLow',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='fiveYearAvgDividendYield',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='freeCashflow',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='insiders',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='operatingCashflow',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='operatingMargins',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='revenuePerShare',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='sharesPercentSharesOut',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='tcps',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='totalCashPerShare',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='totalRevenue',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
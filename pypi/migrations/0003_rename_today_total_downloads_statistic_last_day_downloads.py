# Generated by Django 4.0.6 on 2022-07-21 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pypi', '0002_rename_overall_downloads_statistic_last_month_downloads_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statistic',
            old_name='today_total_downloads',
            new_name='last_day_downloads',
        ),
    ]
# Generated by Django 2.2.9 on 2020-01-02 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coderdojochi', '0031_auto_20200101_2218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='max_age_limitation',
            new_name='override_max_age_limitation',
        ),
        migrations.RenameField(
            model_name='session',
            old_name='min_age_limitation',
            new_name='override_min_age_limitation',
        ),
    ]
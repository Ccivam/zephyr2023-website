# Generated by Django 3.2.5 on 2023-01-24 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zephyr', '0008_rename_sop_ca_statement_of_purpose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ca',
            name='phone_number',
            field=models.BigIntegerField(),
        ),
    ]

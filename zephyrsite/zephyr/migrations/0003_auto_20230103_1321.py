# Generated by Django 3.2.5 on 2023-01-03 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zephyr', '0002_alter_ca_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ca',
            name='permanent_address',
        ),
        migrations.AlterField(
            model_name='ca',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]

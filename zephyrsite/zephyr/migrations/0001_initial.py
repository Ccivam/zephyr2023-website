# Generated by Django 3.2.5 on 2022-11-29 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.PositiveBigIntegerField(max_length=13)),
                ('college', models.CharField(max_length=100)),
                ('year_of_study', models.SmallIntegerField()),
                ('permanent_address', models.TextField()),
                ('pincode', models.IntegerField()),
                ('state', models.CharField(max_length=100)),
            ],
        ),
    ]

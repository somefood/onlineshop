# Generated by Django 3.1.5 on 2021-01-18 23:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('use_from', models.DateTimeField()),
                ('use_to', models.DateTimeField()),
                ('amount', models.IntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(100000)])),
                ('active', models.BooleanField()),
            ],
        ),
    ]

# Generated by Django 2.1.5 on 2019-11-19 09:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191119_0732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Water',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_title', models.CharField(max_length=200)),
                ('water_time', models.DateTimeField(default=datetime.datetime(2019, 11, 19, 9, 55, 4, 224952), verbose_name='Date and Time')),
                ('water_duration', models.DurationField()),
            ],
        ),
        migrations.DeleteModel(
            name='Tutorial',
        ),
    ]
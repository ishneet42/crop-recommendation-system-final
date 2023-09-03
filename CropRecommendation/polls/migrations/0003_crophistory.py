# Generated by Django 4.2.4 on 2023-08-15 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_nitrogen_crop_n_rename_phosphorus_crop_p_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CropHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('N', models.FloatField()),
                ('P', models.FloatField()),
                ('k', models.FloatField()),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('ph', models.FloatField()),
                ('rainfall', models.FloatField()),
                ('notes', models.TextField()),
            ],
        ),
    ]

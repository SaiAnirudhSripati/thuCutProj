# Generated by Django 2.2.9 on 2020-02-02 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listApp', '0004_auto_20200201_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='cat_description',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='list',
            name='list_desc',
            field=models.CharField(max_length=120),
        ),
    ]
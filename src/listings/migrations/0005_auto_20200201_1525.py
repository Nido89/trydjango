# Generated by Django 2.1.7 on 2020-02-01 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20200201_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='summary',
            field=models.TextField(),
        ),
    ]
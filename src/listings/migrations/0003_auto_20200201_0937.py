# Generated by Django 2.1.7 on 2020-02-01 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listings_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]

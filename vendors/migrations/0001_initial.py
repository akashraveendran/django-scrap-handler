# Generated by Django 4.1.5 on 2023-01-26 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilesList',
            fields=[
                ('Vendor_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Vendor_address', models.CharField(max_length=200)),
                ('Vendor_location', models.CharField(max_length=200)),
            ],
        ),
    ]

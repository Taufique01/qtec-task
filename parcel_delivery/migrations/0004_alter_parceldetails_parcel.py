# Generated by Django 3.2 on 2021-04-25 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parcel_delivery', '0003_auto_20210424_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parceldetails',
            name='parcel',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='parcel_details', to='parcel_delivery.parcel'),
        ),
    ]

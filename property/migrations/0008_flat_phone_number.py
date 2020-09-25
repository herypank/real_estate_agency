# Generated by Django 2.2.4 on 2020-09-25 11:45

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20200925_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
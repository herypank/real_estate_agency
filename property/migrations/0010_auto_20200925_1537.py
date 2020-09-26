# Generated by Django 2.2.4 on 2020-09-25 12:37

from django.db import migrations
import phonenumbers


def fix_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        phone_number = flat.owners_phonenumber
        parsing_number = phonenumbers.parse(phone_number, 'RU')
        if phonenumbers.is_valid_number(parsing_number):
            pure_number = phonenumbers.format_number(
                parsing_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            flat.owner_pure_phone = pure_number
            flat.save()


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.owner_pure_phone = None
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20200925_1526'),
    ]

    operations = [
        migrations.RunPython(fix_number, move_backward),
    ]

# Generated by Django 4.0.6 on 2022-07-16 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_delete_user_person_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='age',
            new_name='birthdate',
        ),
    ]

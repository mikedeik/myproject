# Generated by Django 4.0.6 on 2022-07-16 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.DateField(blank=True, null=True),
        ),
    ]
# Generated by Django 5.0.4 on 2024-04-07 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_joined_date_talk_posed_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='talk',
            old_name='posed_date',
            new_name='posted_date',
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-15 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_files_alter_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='files',
            new_name='text',
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-28 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_created=True)),
                ('name', models.CharField(max_length=52)),
                ('description', models.TextField(blank=True, null=True)),
                ('updatedAt', models.DateField(auto_now=True)),
            ],
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-11 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='book_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book.book'),
        ),
    ]

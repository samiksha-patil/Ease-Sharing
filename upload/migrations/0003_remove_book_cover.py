# Generated by Django 3.0.4 on 2020-03-21 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_book_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='cover',
        ),
    ]
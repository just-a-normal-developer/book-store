# Generated by Django 4.2 on 2024-06-05 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]

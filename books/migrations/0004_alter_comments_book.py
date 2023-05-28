# Generated by Django 4.2 on 2023-05-28 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='books.books'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-18 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='is_stock',
            field=models.BooleanField(default=True),
        ),
    ]

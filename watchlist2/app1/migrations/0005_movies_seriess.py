# Generated by Django 4.2.5 on 2023-10-08 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_series'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='Seriess',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.2.5 on 2023-10-04 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='Genre',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='movies',
            name='Language',
            field=models.CharField(default='', max_length=200),
        ),
    ]

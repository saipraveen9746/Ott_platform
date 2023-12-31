# Generated by Django 4.2.5 on 2023-10-04 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('Director', models.CharField(max_length=200)),
                ('Description', models.TextField(max_length=200)),
                ('Release_year', models.PositiveIntegerField(blank=True, null=True)),
                ('Rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('Actor', models.CharField(max_length=200)),
                ('Pop_now', models.BooleanField(default=False)),
                ('image_url', models.CharField(max_length=5000)),
            ],
        ),
    ]

# Generated by Django 2.2.10 on 2023-05-08 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_projectpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpost',
            name='projectImg',
            field=models.ImageField(upload_to='assets/images'),
        ),
    ]

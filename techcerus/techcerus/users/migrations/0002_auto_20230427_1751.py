# Generated by Django 2.2.10 on 2023-04-27 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermsg',
            name='telNumber',
            field=models.IntegerField(),
        ),
    ]

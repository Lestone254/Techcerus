# Generated by Django 2.2.10 on 2023-04-27 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=255)),
                ('telNumber', models.CharField(max_length=255)),
                ('userEmail', models.CharField(max_length=255)),
                ('msgHeading', models.CharField(max_length=255)),
                ('msgBody', models.CharField(max_length=100)),
            ],
        ),
    ]

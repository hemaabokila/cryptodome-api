# Generated by Django 5.1.7 on 2025-03-22 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='addres',
            field=models.CharField(max_length=15),
        ),
    ]

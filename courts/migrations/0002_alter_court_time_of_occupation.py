# Generated by Django 5.1.1 on 2024-09-19 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='time_of_occupation',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
# Generated by Django 4.1 on 2022-08-12 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account_number',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Account Number'),
        ),
    ]

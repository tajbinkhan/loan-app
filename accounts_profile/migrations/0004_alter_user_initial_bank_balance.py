# Generated by Django 4.1 on 2022-08-30 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_profile', '0003_user_initial_bank_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='initial_bank_balance',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]

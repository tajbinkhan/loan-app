# Generated by Django 4.1 on 2022-08-13 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0005_loan_form_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='form_id',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]

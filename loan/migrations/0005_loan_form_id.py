# Generated by Django 4.1 on 2022-08-13 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0004_loan_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='form_id',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
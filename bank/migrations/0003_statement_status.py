# Generated by Django 4.1 on 2022-08-30 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_statement_form_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='statement',
            name='status',
            field=models.CharField(choices=[('Credit', 'Credit'), ('Debit', 'Debit')], default='Credit', max_length=6),
        ),
    ]

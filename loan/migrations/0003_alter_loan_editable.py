# Generated by Django 4.1 on 2022-08-13 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_remove_loan_active_alter_loan_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='editable',
            field=models.CharField(choices=[('Not Applied', 'Not Applied'), ('Requested', 'Requested'), ('Approved', 'Approved'), ('Not Approved', 'Not Approved'), ('Updated', 'Updated')], default='Not Applicable', max_length=14),
        ),
    ]

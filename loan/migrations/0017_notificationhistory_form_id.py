# Generated by Django 4.1 on 2022-08-27 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0016_remove_notificationhistory_money_lender'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationhistory',
            name='form_id',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]

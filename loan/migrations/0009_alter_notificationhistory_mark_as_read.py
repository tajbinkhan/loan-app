# Generated by Django 4.1 on 2022-08-27 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0008_notificationhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationhistory',
            name='mark_as_read',
            field=models.BooleanField(default=False, verbose_name='Mark as Read'),
        ),
    ]
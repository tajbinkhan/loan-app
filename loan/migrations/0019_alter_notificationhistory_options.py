# Generated by Django 4.1 on 2022-08-30 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0018_alter_notificationhistory_mark_as_read'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notificationhistory',
            options={'ordering': ['-updated'], 'verbose_name': 'Notification history', 'verbose_name_plural': 'Notification histories'},
        ),
    ]

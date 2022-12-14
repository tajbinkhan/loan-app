# Generated by Django 4.1 on 2022-08-27 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0014_alter_notificationhistory_mark_as_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationhistory',
            name='editable',
            field=models.CharField(choices=[('Not Applied', 'Not Applied'), ('Requested', 'Requested'), ('Approved', 'Approved'), ('Not Approved', 'Not Approved'), ('Updated', 'Updated')], default='ok', max_length=14),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notificationhistory',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='ok', max_length=8),
            preserve_default=False,
        ),
    ]

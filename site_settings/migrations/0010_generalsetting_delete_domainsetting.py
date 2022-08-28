# Generated by Django 4.1 on 2022-08-27 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0009_alter_emailcontent_notification_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.CharField(max_length=50)),
                ('email_from', models.EmailField(max_length=50, verbose_name='Email From')),
                ('site_name', models.CharField(max_length=20)),
                ('protocol', models.CharField(max_length=5)),
                ('enable_email', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='DomainSetting',
        ),
    ]

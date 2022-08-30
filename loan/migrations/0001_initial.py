# Generated by Django 4.1 on 2022-08-12 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import loan.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PreviousUserList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('money_lender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requested_user', to=settings.AUTH_USER_MODEL, verbose_name='Money Lender')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='Loan Amount')),
                ('return_date', models.DateField(default=django.utils.timezone.now, validators=[loan.models.validate_date], verbose_name='Return Date')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted')], default='Pending', max_length=8)),
                ('editable', models.CharField(choices=[('Not Applicable', 'Not Applicable'), ('Requested', 'Requested'), ('Approved', 'Approved'), ('Not Approved', 'Not Approved'), ('Updated', 'Updated')], default='Not Applicable', max_length=14)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now_add=True, verbose_name='Requested Date')),
                ('money_lender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='money_lender', to=settings.AUTH_USER_MODEL, verbose_name='Money Lender')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
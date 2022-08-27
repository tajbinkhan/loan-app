from datetime import datetime
from django.utils import timezone
from django.db import models
from accounts_profile.models import User
from django.core.exceptions import ValidationError

# Create your models here.
STATUS = (
	('Pending', 'Pending'),
	('Accepted', 'Accepted'),
	('Rejected', 'Rejected'),
)

EDITABLE_STATUS = (
	('Not Applied', 'Not Applied'),
	('Requested', 'Requested'),
	('Approved', 'Approved'),
	('Not Approved', 'Not Approved'),
	('Updated', 'Updated'),
)

def validate_date(date):
	if date < datetime.now().date():
		raise ValidationError("Date cannot be in the past")

class Loan(models.Model):
	form_id = models.CharField(max_length=32, null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	money_lender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='money_lender', verbose_name='Money Lender')
	amount = models.PositiveIntegerField(verbose_name='Loan Amount')
	return_date = models.DateField(default=timezone.now, validators=[validate_date], verbose_name='Return Date')
	status = models.CharField(max_length=8, choices=STATUS, default='Pending')
	editable = models.CharField(max_length=14, choices=EDITABLE_STATUS, default='Not Applied')
	updated = models.DateField(auto_now=True, verbose_name='Updated Date')
	created = models.DateField(auto_now_add=True, verbose_name='Requested Date')

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return f'{self.id} - {self.user.username}({self.form_id}) - {self.created}'

class PreviousUserList(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	money_lender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requested_user', verbose_name='Money Lender')
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return self.user.username

class NotificationHistory(models.Model):
	form_id = models.CharField(max_length=32, null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	amount = models.PositiveIntegerField(verbose_name='Loan Amount')
	loan_user = models.ForeignKey(Loan, on_delete=models.CASCADE, verbose_name='Loan User')
	status = models.CharField(max_length=8, choices=STATUS)
	editable = models.CharField(max_length=14, choices=EDITABLE_STATUS)
	mark_as_read = models.BooleanField(default=False, verbose_name='Mark as Read')
	updated = models.DateTimeField(auto_now=True, verbose_name='Updated Date')
	created = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')

	class Meta:
		verbose_name = 'Notification history'
		verbose_name_plural = 'Notification histories'
		ordering = ['-updated']

	def __str__(self):
		return str(self.loan_user)
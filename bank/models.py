from django.utils import timezone
from django.db import models
from accounts_profile.models import User

# Create your models here.
STATUS = (
	('Credit', 'Credit'),
	('Debit', 'Debit'),
)

class Statement(models.Model):
	form_id = models.CharField(max_length=32, null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	amount = models.PositiveBigIntegerField()
	description = models.CharField(max_length=300)
	entry_date = models.DateField(default=timezone.now)
	status = models.CharField(max_length=6, choices=STATUS, default='Credit')
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return f'{self.user.username} - {self.amount}'

class InterestStatement(models.Model):
	form_id = models.CharField(max_length=32, null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	amount = models.PositiveBigIntegerField()
	tax = models.PositiveBigIntegerField()
	entry_date = models.DateField(default=timezone.now)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return f'{self.user.username} - {self.amount}'
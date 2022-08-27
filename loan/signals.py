import hashlib
from .models import Loan, PreviousUserList, NotificationHistory
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

@receiver(post_save, sender=Loan)
def create_previous_user_list(sender, instance, created, *args, **kwargs):
	if created:
		f_id = Loan.objects.get(id=instance.id)
		hash_object = hashlib.md5(str(f_id.id).encode())
		md5_hash = hash_object.hexdigest()
		f_id.form_id = md5_hash
		f_id.save()
		loan = Loan.objects.filter(user=instance.user, money_lender=instance.money_lender).count()
		previous = PreviousUserList.objects.filter(user=instance.user, money_lender=instance.money_lender).exists()
		if loan == 1:
			if not previous:
				PreviousUserList.objects.create(user=instance.user, money_lender=instance.money_lender)
	else:
		f_id = Loan.objects.get(id=instance.id)
		if not f_id.form_id:
			hash_object = hashlib.md5(str(f_id.id).encode())
			md5_hash = hash_object.hexdigest()
			f_id.form_id = md5_hash
			f_id.save()

@receiver(pre_save, sender=Loan)
def notification_history_update(sender, instance, *args, **kwargs):
	try:
		loan_model = Loan.objects.get(id=instance.id)
		if loan_model.status != instance.status or loan_model.editable != instance.editable:
			if instance.status == 'Accepted' and instance.editable == 'Not Applied':
				NotificationHistory.objects.create(user=instance.user, amount=instance.amount, loan_user=instance, status=instance.status, editable=instance.editable)
				NotificationHistory.objects.create(user=instance.money_lender, amount=instance.amount, loan_user=instance, status=instance.status, editable=instance.editable, mark_as_read=True)
			elif instance.status == 'Accepted' and instance.editable == 'Approved':
				NotificationHistory.objects.create(user=instance.user, amount=instance.amount, loan_user=instance, status=instance.status, editable=instance.editable)
				NotificationHistory.objects.create(user=instance.money_lender, amount=instance.amount, loan_user=instance, status=instance.status, editable=instance.editable, mark_as_read=True)
			elif instance.status == 'Accepted' and instance.editable == 'Not Approved':
				NotificationHistory.objects.create(user=instance.user, amount=instance.amount, loan_user=instance, status=instance.status, editable=instance.editable)
				NotificationHistory.objects.create(user=instance.money_lender, amount=instance.amount, loan_user=instance, status=instance.status, editable=instance.editable, mark_as_read=True)
			elif instance.status == 'Accepted' and instance.editable == 'Updated':
				NotificationHistory.objects.create(user=instance.user, amount=instance.amount, loan_user=instance, status=instance.status, editable=instance.editable)
				NotificationHistory.objects.create(user=instance.money_lender, amount=instance.amount, loan_user=instance, status=instance.status, editable=instance.editable, mark_as_read=True)
			elif instance.status == 'Rejected' and instance.editable == 'Not Applied':
				NotificationHistory.objects.create(user=instance.user, amount=instance.amount, loan_user=instance, status=instance.status, editable=instance.editable)
				NotificationHistory.objects.create(user=instance.money_lender, amount=instance.amount, loan_user=instance, status=instance.status, editable=instance.editable, mark_as_read=True)
	except:
		pass

@receiver(post_save, sender=NotificationHistory)
def notification_create(sender, instance, created, *args, **kwargs):
	if created:
		f_id = NotificationHistory.objects.get(id=instance.id)
		if not f_id.form_id:
			hash_object = hashlib.md5(str(f_id.id).encode())
			md5_hash = hash_object.hexdigest()
			f_id.form_id = md5_hash
			f_id.save()
	else:
		f_id = NotificationHistory.objects.get(id=instance.id)
		if not f_id.form_id:
			hash_object = hashlib.md5(str(f_id.id).encode())
			md5_hash = hash_object.hexdigest()
			f_id.form_id = md5_hash
			f_id.save()

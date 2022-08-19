import hashlib
from .models import Loan, PreviousUserList
from django.db.models.signals import post_save
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

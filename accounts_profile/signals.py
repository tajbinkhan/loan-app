from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from .utils import generate_string, generate_digit

@receiver(post_save, sender=User)
def account_number_create(sender, created, instance, *args, **kwargs):
	if created:
		if instance.account_number is None:
			if len(str(instance.id)) == 1:
				instance.account_number = f'AC{generate_digit(3)}{generate_string(3)}{generate_digit(7)}{str(instance.id)}'
				instance.save()
			elif len(str(instance.id)) == 2:
				instance.account_number = f'AC{generate_digit(3)}{generate_string(3)}{generate_digit(6)}{str(instance.id)}'
				instance.save()
			elif len(str(instance.id)) == 3:
				instance.account_number = f'AC{generate_digit(3)}{generate_string(3)}{generate_digit(5)}{str(instance.id)}'
				instance.save()
			elif len(str(instance.id)) == 4:
				instance.account_number = f'AC{generate_digit(3)}{generate_string(3)}{generate_digit(4)}{str(instance.id)}'
				instance.save()
	else:
		if instance.account_number is None:
			if len(str(instance.id)) == 1:
				instance.account_number = f'AC{generate_digit(3)}{generate_string(3)}{generate_digit(7)}{str(instance.id)}'
				instance.save()
			elif len(str(instance.id)) == 2:
				instance.account_number = f'AC{generate_digit(3)}{generate_string(3)}{generate_digit(6)}{str(instance.id)}'
				instance.save()
			elif len(str(instance.id)) == 3:
				instance.account_number = f'AC{generate_digit(3)}{generate_string(3)}{generate_digit(5)}{str(instance.id)}'
				instance.save()
			elif len(str(instance.id)) == 4:
				instance.account_number = f'AC{generate_digit(3)}{generate_string(3)}{generate_digit(4)}{str(instance.id)}'
				instance.save()
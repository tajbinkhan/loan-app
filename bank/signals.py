import hashlib
from .models import Statement, InterestStatement
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Statement)
def statement_create(sender, instance, created, *args, **kwargs):
	if created:
		f_id = Statement.objects.get(id=instance.id)
		if not f_id.form_id:
			hash_object = hashlib.md5(str(f_id.id).encode())
			md5_hash = hash_object.hexdigest()
			f_id.form_id = md5_hash
			f_id.save()
	else:
		f_id = Statement.objects.get(id=instance.id)
		if not f_id.form_id:
			hash_object = hashlib.md5(str(f_id.id).encode())
			md5_hash = hash_object.hexdigest()
			f_id.form_id = md5_hash
			f_id.save()

@receiver(post_save, sender=InterestStatement)
def tax_statement_create(sender, instance, created, *args, **kwargs):
	if created:
		f_id = InterestStatement.objects.get(id=instance.id)
		if not f_id.form_id:
			hash_object = hashlib.md5(str(f_id.id).encode())
			md5_hash = hash_object.hexdigest()
			f_id.form_id = md5_hash
			f_id.save()
	else:
		f_id = InterestStatement.objects.get(id=instance.id)
		if not f_id.form_id:
			hash_object = hashlib.md5(str(f_id.id).encode())
			md5_hash = hash_object.hexdigest()
			f_id.form_id = md5_hash
			f_id.save()
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from core.filename import profile_upload_image_path

# Create your models here.

class User(AbstractUser):
	email = models.EmailField(max_length=120, blank=False, null=False, unique=True)
	profile_pic = models.ImageField(upload_to=profile_upload_image_path, null=True, blank=True, default='avatar.png', verbose_name='Profile picture')
	account_number = models.CharField(max_length=16, verbose_name='Account Number', null=True, blank=True)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		try:
			img = Image.open(self.profile_pic.path)
			if img.height > 400 or img.width > 400:
				output_size = (400, 400)
				img.thumbnail(output_size)
				img.save(self.profile_pic.path)
		except:
			pass
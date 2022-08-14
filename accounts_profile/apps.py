from django.apps import AppConfig


class AccountsProfileConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'accounts_profile'
	verbose_name = 'Accounts & Profile'

	def ready(self):
		import accounts_profile.signals

from django.contrib import admin
from .models import GeneralSetting, EmailContent

# Register your models here.
class GeneralSettingAdmin(admin.ModelAdmin):
	list_display = ('site_name', 'protocol', 'domain_name', 'email_from', 'enable_email')
	save_on_top = True

class EmailContentAdmin(admin.ModelAdmin):
	list_display = ('notification_name', 'subject')
	save_on_top = True

admin.site.register(GeneralSetting, GeneralSettingAdmin)
admin.site.register(EmailContent, EmailContentAdmin)
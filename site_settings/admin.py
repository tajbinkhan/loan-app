from django.contrib import admin
from .models import DomainSetting, EmailContent

# Register your models here.
class DomainSettingAdmin(admin.ModelAdmin):
	list_display = ('site_name', 'protocol', 'domain_name', 'email_from')
	save_on_top = True

class EmailContentAdmin(admin.ModelAdmin):
	list_display = ('notification_name', 'subject')
	save_on_top = True

admin.site.register(DomainSetting, DomainSettingAdmin)
admin.site.register(EmailContent, EmailContentAdmin)
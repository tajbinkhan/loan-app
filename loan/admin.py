from django.contrib import admin
from .models import Loan, PreviousUserList, NotificationHistory

# Register your models here.
class LoanAdmin(admin.ModelAdmin):
	list_display = ('user', 'money_lender', 'amount', 'created', 'return_date', 'status', 'editable', 'updated', 'form_id')

class PreviousUserListAdmin(admin.ModelAdmin):
	list_display = ('user', 'money_lender', 'created')

class NotificationHistoryAdmin(admin.ModelAdmin):
	list_display = ('loan_user', 'user', 'mark_as_read', 'status', 'editable', 'updated', 'created')

admin.site.register(Loan, LoanAdmin)
admin.site.register(PreviousUserList, PreviousUserListAdmin)
admin.site.register(NotificationHistory, NotificationHistoryAdmin)
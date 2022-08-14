from django.contrib import admin
from .models import Loan, PreviousUserList

# Register your models here.
class LoanAdmin(admin.ModelAdmin):
	list_display = ('user', 'money_lender', 'amount', 'created', 'return_date', 'status', 'editable', 'updated', 'form_id')

class PreviousUserListAdmin(admin.ModelAdmin):
	list_display = ('user', 'money_lender', 'created')

admin.site.register(Loan, LoanAdmin)
admin.site.register(PreviousUserList, PreviousUserListAdmin)
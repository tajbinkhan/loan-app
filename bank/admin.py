from django.contrib import admin
from .models import Statement, InterestStatement

# Register your models here.
class StatementAdmin(admin.ModelAdmin):
	list_display = ('user', 'amount', 'entry_date', 'description', 'status', 'created', 'updated')
	radio_fields = {'status': admin.VERTICAL}

class InterestStatementAdmin(admin.ModelAdmin):
	list_display = ('user', 'amount', 'tax', 'entry_date', 'created', 'updated')

admin.site.register(Statement, StatementAdmin)
admin.site.register(InterestStatement, InterestStatementAdmin)
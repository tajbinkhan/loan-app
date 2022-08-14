from django.contrib import admin
from .models import User
from .forms import UserModelForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

# Register your models here.
class UserAdmin(UserAdmin):
	model = User
	add_form = UserModelForm
	save_on_top = True
	ordering = ('-date_joined', )
	fieldsets = (*UserAdmin.fieldsets, ('User Profile', {'fields': ('profile_pic', 'account_number')}))
	list_display = ('username', 'account_number', 'email', 'first_name', 'last_name', 'is_superuser', 'date_joined', 'last_login')
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2'),
		}),
	)

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
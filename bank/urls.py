from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.urls import reverse_lazy

urlpatterns = [
	path('statement/', views.statement_list, name='statement_list'),
	path('statement/add/', views.statement_create, name='statement_create'),
	path('statement/update/<str:form_id>/', views.statement_update, name='statement_update'),
	path('statement/delete/<str:form_id>/', views.statement_delete, name='statement_delete'),
	path('interest/add/', views.interest_statement_create, name='interest_statement_create'),
	path('interest/update/<str:form_id>/', views.interest_statement_update, name='interest_statement_update'),
	path('interest/delete/<str:form_id>/', views.interest_statement_delete, name='interest_statement_delete'),

	# HTMX validation
	path('statement/check-amount/', views.check_amount, name='check_amount'),
	path('statement/check-entry-date/', views.check_entry_date, name='check_entry_date'),
	path('interest/check-interest-amount/', views.check_interest_amount, name='check_interest_amount'),
	path('interest/check-interest-tax/', views.check_interest_tax, name='check_interest_tax'),
	path('interest/check-interest-entry-date/', views.check_interest_entry_date, name='check_interest_entry_date'),
]
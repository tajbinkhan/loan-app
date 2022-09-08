from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.urls import reverse_lazy

urlpatterns = [
	path('', views.dashboard, name='dashboard'),
	path('request/', RedirectView.as_view(url=reverse_lazy('dashboard'), permanent=False)),
	path('request/update/', RedirectView.as_view(url=reverse_lazy('dashboard'), permanent=False)),
	path('request/update/approve/', RedirectView.as_view(url=reverse_lazy('dashboard'), permanent=False)),
	path('request/update/deny/', RedirectView.as_view(url=reverse_lazy('dashboard'), permanent=False)),
	path('notification/approve/', RedirectView.as_view(url=reverse_lazy('notification'), permanent=False)),
	path('notification/deny/', RedirectView.as_view(url=reverse_lazy('notification'), permanent=False)),
	path('loan/', RedirectView.as_view(url=reverse_lazy('dashboard'), permanent=False)),
	path('loan/delete/', RedirectView.as_view(url=reverse_lazy('dashboard'), permanent=False)),
	path('form/update/', RedirectView.as_view(url=reverse_lazy('loan_form'), permanent=False)),
	path('requested/', views.loan_requested, name='loan_requested'),
	path('form/', views.loan_form, name='loan_form'),
	path('form/<str:account_number>/', views.loan_request_again, name='loan_request_again'),
	path('form/update/<str:form_id>/', views.update_loan, name='update_loan'),
	path('list/', views.previous_user_list, name='previous_user_list'),
	path('loan/delete/<str:form_id>/', views.loan_delete, name='loan_delete'),
	path('notification/', views.notification, name='notification'),
	path('notification/approve/<str:form_id>/', views.notification_approve, name='notification_approve'),
	path('notification/deny/<str:form_id>/', views.notification_deny, name='notification_deny'),
	path('request/update/<str:form_id>/', views.request_for_update, name='request_for_update'),
	path('request/update/approve/<str:form_id>/', views.request_for_update_approve, name='request_for_update_approve'),
	path('request/update/deny/<str:form_id>/', views.request_for_update_deny, name='request_for_update_deny'),
	path('read/<str:form_id>/', views.mark_as_read, name='mark_as_read'),

	# HTMX Check
	path('check-account-number/', views.check_account_number, name='check_account_number'),
	path('check-account-name/', views.check_account_name, name='check_account_name'),
	path('check-return-date/', views.check_return_date, name='check_return_date'),
]
from django.urls import path
from . import views

urlpatterns = [
	path('accounts/profile/', views.profile, name='profile'),
	path('accounts/profile/update/', views.update_profile, name='update_profile'),
	path('profile/<str:account_number>/', views.show_profile, name='show_profile'),
]
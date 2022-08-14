from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.urls import reverse_lazy

urlpatterns = [
	path('admin/', admin.site.urls),
	path('accounts/', RedirectView.as_view(url=reverse_lazy('account_login'), permanent=False)),
	path('accounts/', include('allauth.urls')),
	path('', include('loan.urls')),
	path('', include('accounts_profile.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
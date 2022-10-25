from django.contrib import admin
from core import settings
from core import views
from django.views.generic import RedirectView
from django.urls import path, include
from simple_sso.sso_client.client import Client

client = Client(settings.SSO_SERVER, settings.SSO_PUBLIC_KEY, settings.SSO_PRIVATE_KEY)

urlpatterns = [
    path('', RedirectView.as_view(url='home/')),
    path('admin/', admin.site.urls),
    path('login/', include(client.get_urls())),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', views.index, name='home'),
]

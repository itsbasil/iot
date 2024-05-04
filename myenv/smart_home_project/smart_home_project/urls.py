from django.contrib import admin
from django.urls import path, include
from devices import views as device_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Django's built-in authentication URLs
    path('', device_views.home, name='home'),
    path('toggle/<int:light_id>/', device_views.toggle_light, name='toggle_light'),
]

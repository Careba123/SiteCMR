from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect
from django.conf import settings  # Importă setările
from django.conf.urls.static import static  # Importă static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cmr_app.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/profile/', lambda request: HttpResponseRedirect('/dashboard/')),
]

# Adaugă configurarea pentru fișierele media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views

app_name = 'cmr_app'

urlpatterns = [
    path('upload/', views.upload_cmr, name='upload_cmr'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

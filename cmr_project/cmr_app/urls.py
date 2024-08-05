from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_cmr, name='upload_cmr'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

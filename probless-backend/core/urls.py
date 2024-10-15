from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
	path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
]
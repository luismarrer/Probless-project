from django.urls import path
from .views import OwnerSignupView, UserLoginView, DashboardView, LogoutView


urlpatterns = [
    path('signup/owner/', OwnerSignupView.as_view(), name='signup_owner'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
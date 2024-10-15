from django.urls import path
from . import views


urlpatterns = [
    path('signup/owner/', views.OwnerSignupView.as_view(), name='signup_owner'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('create-user/', views.CreateUserView.as_view(), name='create_user')
]

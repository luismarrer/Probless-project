from django.urls import path
from . import views


urlpatterns = [
    path('signup/owner/', views.OwnerSignupView.as_view(), name='signup_owner'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('create-user/', views.CreateUserView.as_view(), name='create_user'),
    path('show_users/', views.owner_users_view, name='show_users'),
    path('update_user/<int:user_id>/', views.update_user, name='update_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('account/update_user/<int:user_id>/', views.update_user, name='update_user'),
    path('account/change_password/<int:user_id>/', views.change_password, name='change_password'),
    path('profile/<int:user_id>/', views.view_detail_user, name='view_detail_user'),
]

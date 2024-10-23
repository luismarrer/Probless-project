from django.urls import path
from . import views


urlpatterns = [
	path('', views.show_workspaces, name='show_workspaces'),
	path('<int:workspace_id>/', views.workspace_detail, name='workspace_detail'),
	path('create/', views.create_workspace, name='create_workspace'),
	path('<int:workspace_id>/create/department/', views.create_department, name='create_department'),
	path('<int:workspace_id>/update/', views.update_workspace, name='update_workspace'),
    path('<int:workspace_id>/delete/', views.delete_workspace, name='delete_workspace'),
    path('<int:workspace_id>/department/<int:department_id>/update/', views.update_department, name='update_department'),
    path('<int:workspace_id>/department/<int:department_id>/delete/', views.delete_department, name='delete_department'),
]
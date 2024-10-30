from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
	path('<int:workspace_id>/<int:department_id>/dashboard/', views.DashboardView.as_view(), name='dashboard'),
	path('<int:workspace_id>/<int:department_id>/create_ticket/', views.create_ticket, name='create_ticket'),
	path('<int:workspace_id>/<int:department_id>/ticket/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
	path('<int:workspace_id>/<int:department_id>/closed_tickets/', views.tickets_history, name='tickets_history'),
	path('error/', views.error, name='error_page'),
]
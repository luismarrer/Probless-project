from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Ticket
from .forms import TicketForm
from workspace.models import Workspace

# Create your views here.


def home(request):
    return render(request, 'home.html')

# Dashboard view


class DashboardView(LoginRequiredMixin, View):
    login_url = '/login/'  # Redirige a esta URL si no está autenticado
    # Opción para redirigir al usuario después de autenticarse
    redirect_field_name = 'next'

    def get(self, request, workspace_name, department_name):
        workspace = Workspace.objects.get(name=workspace_name)
        department = workspace.department_set.get(name=department_name)
        tickets = Ticket.objects.filter(user_id=request.user)
        return render(request, 'dashboard.html',
                      {
                          'workspace': workspace,
                          'department': department,
                          'tickets': tickets
                      })

# Ticket view


@login_required
def create_ticket(request, workspace_id, department_id):
    """
    Create ticket view - POST(CREATE)
    """
    workspace = Workspace.objects.get(id=workspace_id)
    department = workspace.department_set.get(id=department_id)
    form = TicketForm(workspace=workspace)
    print(form)
    if request.method == 'GET':
        return render(request, 'create_ticket.html',
                      {
                          'form': form
                      })
    else:
        try:
            form = TicketForm(request.POST)
            new_ticket = form.save(commit=False)
            new_ticket.user_id = request.user
            new_ticket.save()
            return redirect('dashboard', workspace_name=workspace.name, department_name=department.name)
        except ValueError:
            return render(request, 'create_ticket.html',
                          {
                              'form': form,
                              'error': 'Bad data passed in. Try again'
                          })


@login_required
def ticket_detail(request, ticket_id, workspace_id, department_id):
	"""
	Ticket detail view - GET(READ)
	"""
	ticket = Ticket.objects.get(id=ticket_id)
	return render(request, 'ticket_detail.html',
				  {
					  'ticket': ticket
				  })

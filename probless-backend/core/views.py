from django.shortcuts import get_object_or_404, render, redirect
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
        workspace = Workspace.objects.get(name=workspace_name, user=request.user)
        department = workspace.department_set.get(name=department_name)
        tickets = Ticket.objects.filter(user_id=request.user)
        tickets_department = Ticket.objects.filter(assigned_department_id=department)
        return render(request, 'dashboard.html',
                      {
                          'workspace': workspace,
                          'department': department,
                          'tickets': tickets,
                          'tickets_department': tickets_department
                      })


# Ticket view
@login_required
def create_ticket(request, workspace_id, department_id):
    """
    Create ticket view - POST(CREATE)
    """
    workspace = Workspace.objects.get(id=workspace_id)
    department = workspace.department_set.get(id=department_id)
    if request.method == 'GET':
        form = TicketForm(workspace=workspace, show_documentation=False)
        return render(request, 'create_ticket.html',
                      {
                          'form': form
                      })
    else:
        try:
            form = TicketForm(request.POST, workspace=workspace)
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
def ticket_detail(request, ticket_id):
    """
    View for ticket details - GET (READ)
    """
    ticket = get_object_or_404(Ticket, id=ticket_id)
    
    # Verifica si el usuario es el propietario del ticket o un administrador
    if ticket.user_id == request.user or request.user.role == 'admin':
        if request.method == 'POST':
            # Lógica para manejar el ticket (solo para admins)
            documentation = request.POST.get('documentation')
            ticket.documentation = documentation  # Asegúrate de que el campo exista en el modelo Ticket
            ticket.status = 'closed'  # O cualquier lógica que necesites
            ticket.save()
            return redirect('ticket_detail', ticket_id=ticket.id)
        else:
            # Renderiza la plantilla con los detalles del ticket
            return render(request, 'ticket_detail.html', {'ticket': ticket})
    else:
        return render(request, 'ticket_detail.html', {
            'ticket': ticket,
            'error': 'You do not have permission to manage this ticket.'
        })

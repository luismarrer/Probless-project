from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Ticket
from .forms import TicketForm
from workspace.models import Department, Workspace

# Create your views here.


def home(request):
    return render(request, 'home.html')


# Dashboard view
class DashboardView(LoginRequiredMixin, View):
    login_url = '/login/'  # Redirige a esta URL si no está autenticado
    # Opción para redirigir al usuario después de autenticarse
    redirect_field_name = 'next'

    def get(self, request, workspace_name, department_name):
        try:
            # Buscar el departamento al que pertenece el usuario y obtener el workspace
            department = Department.objects.get(name=department_name, workspace_id__name=workspace_name)

            # Asegurarse de que el usuario esté en el departamento
            if not request.user.is_owner and request.user.dept != department:
                return redirect('error_page')  # Puedes redirigir a una página de error si el usuario no pertenece

            workspace = department.workspace_id  # Obtener el workspace del departamento
            tickets = Ticket.objects.filter(user_id=request.user).exclude(status='Closed')
            tickets_department = Ticket.objects.filter(assigned_department_id=department).exclude(status='Closed')


            return render(request, 'dashboard.html',
                          {
                              'workspace': workspace,
                              'department': department,
                              'tickets': tickets,
                              'tickets_department': tickets_department,
                          })
        except Department.DoesNotExist:
            return redirect('error_page')

# Ticket view
@login_required
def create_ticket(request, workspace_id, department_id):
    """
    Create ticket view - POST(CREATE)
    """
    workspace = Workspace.objects.get(id=workspace_id)
    department = Department.objects.get(id=department_id)
    if request.method == 'GET':
        form = TicketForm(workspace=workspace, show_documentation=False)
        return render(request, 'create_ticket.html',
                      {
                          'form': form,
                          'workspace_name': workspace.name,
                          'department_name': department.name,
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
                                'workspace_name': workspace.name,
                                'department_name': department.name,
                                'error': 'Bad data passed in. Try again',
                          })


@login_required
def ticket_detail(request, ticket_id, workspace_id, department_id):
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
            ticket.status = 'Closed'  # O cualquier lógica que necesites
            ticket.save()

            workspace_name = ticket.assigned_department_id.workspace_id.name
            department_name = ticket.assigned_department_id.name
            return redirect('dashboard', workspace_name=workspace_name, department_name=department_name)
        else:
            # Renderiza la plantilla con los detalles del ticket
            return render(request, 'ticket_detail.html', {'ticket': ticket})
    else:
        return render(request, 'ticket_detail.html', {
            'ticket': ticket,
            'error': 'You do not have permission to manage this ticket.'
        })

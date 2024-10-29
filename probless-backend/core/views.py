from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Ticket
from .forms import TicketForm
from workspace.models import Department, Workspace
from openai import OpenAI

# Create your views here.

# OpenAI client
client = OpenAI(api_key=settings.OPENAI_API_KEY)

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
                          'ai_response': None,
                      })
    else:
        form = TicketForm(request.POST, workspace=workspace)

        if 'use_ai' in request.POST and form.is_valid():
            description = form.cleaned_data["description"]
            ai_response = get_ai_solution(description)

            return render(request, 'create_ticket.html', {
                'form': form,
                'workspace_name': workspace.name,
                'department_name': department.name,
                'ai_response': ai_response,
            })

        if form.is_valid():
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

def tickets_history(request, workspace_id, department_id):
    workspace = Workspace.objects.filter(id=workspace_id)
    department = Department.objects.get(id=department_id, workspace_id=workspace_id)
    closed_tickets = Ticket.objects.filter(user_id=request.user, status='Closed', assigned_department_id=department)

    return render(request, 'tickets_history.html', {
        'closed_tickets': closed_tickets,
        'workspace_name': workspace,
        'department_name': department.name,
    })



def get_ai_solution(description):

    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": """You are a helpful assistan taht solves problem from users tickets.
                                                Your answer can. Your answer should not be more than 5 solutions, try not to be more than 130 words"""},
                {"role": "user", "content": description},
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error in AI processing: {str(e)}"
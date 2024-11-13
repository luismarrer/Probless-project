from django.db.models import Case, When, Value, IntegerField
from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Ticket
from .forms import TicketForm
from workspace.models import Department, Workspace
from openai import OpenAI
import re


# OpenAI client
client = OpenAI(api_key=settings.OPENAI_API_KEY)


def home(request):
    return render(request, 'home.html')


# Dashboard view
class DashboardView(LoginRequiredMixin, View):
    # Redirect to this URL if it is not authenticated
    login_url = '/login/'

    # Option to redirect the user after authenticating
    redirect_field_name = 'next'

    def get(self, request, workspace_id, department_id):
        try:
            # Find the department to which the user belongs
            department = Department.objects.get(
                id=department_id, workspace_id=workspace_id)

            # Make sure the user is in the department
            if not request.user.is_owner and request.user.dept != department:
                return redirect('error_page')

                # Get the department workspace
            workspace = department.workspace_id
            tickets = Ticket.objects.filter(
                user_id=request.user).exclude(status='closed')
            tickets_department = Ticket.objects.filter(
                assigned_department_id=department).exclude(status='closed').annotate(
                priority_order=Case(
                    When(priority="high", then=Value(1)),
                    When(priority="medium", then=Value(2)),
                    When(priority="low", then=Value(3)),
                    output_field=IntegerField(),
                )
            ).order_by('priority_order')

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
        form = TicketForm(workspace=workspace, show_documentation=False, show_status=False)
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

            processed_response = []
            for line in ai_response.splitlines():
                line = line.strip()  # Limpiar espacios en blanco
                if re.match(r'^\s*[\*\-•]\s*', line) or re.match(r'^\s*\d+\.\s*', line):
                    # Convertir bullet a elemento de lista
                    processed_response.append(f"<li>{line}</li>")
                elif line:  # Si no está vacío, lo agrega como párrafo
                    processed_response.append(f"<p>{line}</p>")

            full_response = "<br/>".join(processed_response)

            return render(request, 'create_ticket.html', {
                'form': form,
                'workspace_name': workspace.id,
                'department_name': department.id,
                'ai_response': full_response,
            })

        if form.is_valid():
            try:
                form = TicketForm(request.POST, workspace=workspace)
                new_ticket = form.save(commit=False)
                new_ticket.user_id = request.user
                new_ticket.incoming_department_id = department
                new_ticket.save()
                return redirect('dashboard', workspace_id=workspace.id, department_id=department.id)
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

    if ticket.user_id == request.user or request.user.role == 'admin':
        if request.method == 'POST':
            form = TicketForm(request.POST, workspace=ticket.assigned_department_id.workspace_id, instance=ticket, show_documentation=True, show_status=True)

            if form.is_valid():

                documentation_value = form.cleaned_data.get('documentation', '')

                cleaned_documentation = documentation_value.strip()  # Eliminate the spaces at the start and the end
                if not cleaned_documentation or cleaned_documentation == "<p>&nbsp;</p>":
                    documentation_value = ''

                if form.cleaned_data['status'] == 'closed' and not documentation_value:
                    messages.error(request, "Documentation is obligatory")
                    return render(request, 'ticket_detail.html', {'ticket': ticket, 'form':form})

                else:
                    form.save()
                    return redirect('dashboard', workspace_id=workspace_id, department_id=department_id)

            else:
                messages.error(request, "There was an error in the submission.")
        else:
            form = TicketForm(instance=ticket, workspace=ticket.assigned_department_id.workspace_id, show_documentation=True, show_status=True)
        return render(request, 'ticket_detail.html', {'ticket': ticket, 'form':form})
    else:
        return render(request, 'ticket_detail.html', {
            'ticket': ticket,
            'error': 'You do not have permission to manage this ticket.'
        })


@login_required
def tickets_history(request, workspace_id, department_id):
    workspace = Workspace.objects.get(id=workspace_id)
    department = Department.objects.get(
        id=department_id, workspace_id=workspace.id)
    closed_tickets = Ticket.objects.filter(
        user_id=request.user, status='closed', assigned_department_id=department)

    return render(request, 'tickets_history.html', {
        'closed_tickets': closed_tickets,
        'workspace': workspace,
        'department': department,
    })


def get_ai_solution(description):

    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": """You are a helpful assistan taht solves problem from users tickets.
                                                 Make the user feel that you are concerned about their problem.  There is no follow-up on the issue.
                                                 Your answer should not be more than 6 solutions, try not to be more than 130 words"""},
                {"role": "user", "content": description},
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error in AI processing: {str(e)}"


@login_required
def manage_tickets(request, workspace_id, department_id):
    workspace = Workspace.objects.get(id=workspace_id)
    department = Department.objects.get(id=department_id)
    tickets_department = Ticket.objects.filter(
        assigned_department_id=department).exclude(status='closed').annotate(
            priority_order=Case(
                When(priority="high", then=Value(1)),
                When(priority="medium", then=Value(2)),
                When(priority="low", then=Value(3)),
                output_field=IntegerField(),
            )).order_by('priority_order')

    return render(request, 'show_manage_tickets.html', {
        'tickets_department': tickets_department,
        'workspace': workspace,
        'department': department,
    })


@login_required
def my_tickets(request, workspace_id, department_id):
    workspace = Workspace.objects.get(id=workspace_id)
    department = Department.objects.get(id=department_id)
    tickets = Ticket.objects.filter(
        user_id=request.user).exclude(status='closed').annotate(
            priority_order=Case(
				When(priority="high", then=Value(1)),
				When(priority="medium", then=Value(2)),
				When(priority="low", then=Value(3)),
				output_field=IntegerField(),
			)).order_by('priority_order')

    return render(request, 'show_my_tickets.html', {
        'tickets': tickets,
        'workspace': workspace,
        'department': department,
    })


# Error view
def error(request):
    return render(request, 'error_page.html')

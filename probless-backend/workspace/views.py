from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Workspace, Department
from .forms import WorkspaceForm, DepartmentForm

# Create your views here.


# Workspace views

@login_required
def show_workspaces(request):
    """
    Workspaces view for authenticated users - GET(READ)
    """
    workspaces = Workspace.objects.filter(user=request.user)
    return render(request, 'show_workspaces.html',
                  {
                      'workspaces': workspaces
                  })


@login_required
def workspace_detail(request, workspace_id):
    """
    Workspace view for authenticated users - GET(READ)
    """
    workspace = Workspace.objects.get(pk=workspace_id)
    departments = Department.objects.filter(workspace_id=workspace)
    return render(request, 'workspace_detail.html',
                  {
                      'workspace': workspace,
                      'departments': departments
                  })


@login_required
def create_workspace(request):
    """
    Create workspace view - POST(CREATE)
    """
    if request.method == 'GET':
        return render(request, 'create_workspace.html',
                      {
                          'form': WorkspaceForm
                      })
    else:
        try:
            form = WorkspaceForm(request.POST)
            if form.is_valid():
                workspace_name = form.cleaned_data['name']
                existing_workspace = Workspace.objects.filter(user=request.user, name=workspace_name).exists()

                if existing_workspace:
                      return render(request, 'create_workspace.html', {
                        'form': form,
                        'error': f'You already have a workspace named "{workspace_name}". Please choose a different name.'
                    })
            new_workspace = form.save(commit=False)
            new_workspace.user = request.user
            new_workspace.save()
            return redirect('show_workspaces')
        except ValueError:
            return render(request, 'create_workspace.html',
                          {
                              'form': WorkspaceForm,
                              'error': 'Bad data passed in. Try again'
                          })


# Department views

@login_required
def create_department(request, workspace_id):
    """
    Create department view - POST(CREATE)
    """
    if request.method == 'GET':
        return render(request, 'create_department.html',
                      {
                          'form': DepartmentForm
                      })
    else:
        try:
            form = DepartmentForm(request.POST)
            if form.is_valid():
                department_name = form.cleaned_data['name']  # Obtener el nombre del departamento
                workspace = Workspace.objects.get(pk=workspace_id)  # Obtener el workspace actual

                # Verificar si ya existe un departamento con el mismo nombre en este workspace
                existing_department = Department.objects.filter(workspace_id=workspace, name=department_name).exists()

                if existing_department:
                    return render(request, 'create_department.html', {
                        'form': form,
                        'error': f'A department with the name "{department_name}" already exists in this workspace. Please choose a different name.'
                    })

                new_department = form.save(commit=False)  # Crear el nuevo departamento pero no guardarlo aún
                new_department.user = request.user
                new_department.workspace_id = workspace  # Asignar el workspace
                new_department.save()  # Guardar el nuevo departamento
                return redirect('workspace_detail', workspace_id)
            else:
                return render(request, 'create_department.html', {
                    'form': form,
                    'error': 'There were errors in your form submission. Please correct them and try again.'
                })
        except ValueError:
            return render(request, 'create_department.html',
                          {
                              'form': DepartmentForm,
                              'error': 'Bad data passed in. Try again'
                          })


@login_required
def show_departments(request):
    """
    Department view for all users - GET(READ)
    """
    departments = Department.objects.all()
    return render(request, 'show_departments.html',
                  {
                      'departments': departments
                  })

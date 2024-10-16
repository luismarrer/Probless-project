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
            new_department = form.save(commit=False)
            new_department.user = request.user
            workspace = Workspace.objects.get(pk=workspace_id)
            new_department.workspace_id = workspace
            new_department.save()
            return redirect('workspace_detail', workspace_id)
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

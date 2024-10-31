from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Workspace, Department
from .forms import WorkspaceForm, DepartmentForm


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
    departments = Department.objects.filter(
        workspace_id=workspace, user=request.user)

    workspace_name = workspace.name
    return render(request, 'workspace_detail.html',
                  {
                      'workspace': workspace,
                      'workspace_name': workspace_name,
                      'departments': departments,
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
                existing_workspace = Workspace.objects.filter(
                    user=request.user, name=workspace_name).exists()

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


@login_required
def update_workspace(request, workspace_id):
    # Recieve workspace or return 404 error
    workspace = get_object_or_404(Workspace, id=workspace_id)

    if request.method == 'POST':
        form = WorkspaceForm(request.POST, instance=workspace)
        if form.is_valid():
            form.save()
            return redirect('workspace_detail', workspace_id=workspace.id)
    else:
        form = WorkspaceForm(instance=workspace)

    return render(request, 'update_workspace.html', {'form': form, 'workspace': workspace})


@login_required
def delete_workspace(request, workspace_id):
    workspace = get_object_or_404(Workspace, id=workspace_id)

    if workspace:
        workspace.delete()
        # Redirect to a list of workspaces
        return redirect('show_workspaces')

    return redirect('error_page')


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
                # Get the name of a departmnet
                department_name = form.cleaned_data['name']
                workspace = Workspace.objects.get(
                    pk=workspace_id)  # Get the actual workspce

                # Verify if a department with the same name exist in that worksapce
                existing_department = Department.objects.filter(
                    workspace_id=workspace, name=department_name).exists()

                if existing_department:
                    return render(request, 'create_department.html', {
                        'form': form,
                        'error': f'A department with the name "{department_name}" already exists in this workspace. Please choose a different name.'
                    })

                # Create new department without saving it
                new_department = form.save(commit=False)
                new_department.user = request.user
                new_department.workspace_id = workspace  # Assign the workspace
                new_department.save()  # Save new department
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
def update_department(request, department_id, workspace_id):
    workspace = get_object_or_404(Workspace, id=workspace_id)
    # Recieve department or throw error code 404
    department = get_object_or_404(
        Department, id=department_id, workspace_id=workspace)

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('workspace_detail',  workspace_id=workspace.id)
    else:
        form = DepartmentForm(instance=department)

    return render(request, 'update_department.html',
                  {'form': form,
                   'department': department,
                   'workspace': workspace
                   })


@login_required
def delete_department(request, workspace_id, department_id):
    workspace = get_object_or_404(Workspace, id=workspace_id)
    department = get_object_or_404(
        Department, id=department_id, workspace_id=workspace)

    if department:
        department.delete()
        return redirect('workspace_detail', workspace_id=workspace.id)

    return redirect('error_page')

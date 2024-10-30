from pyexpat.errors import messages
from django.views import View
from workspace.models import Department
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import ChangePasswordForm, OwnerSignupForm, LoginForm, CreateUserForm, UpdateUserForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.views.decorators.csrf import csrf_protect


# Owner sign up view
class OwnerSignupView(View):
    def get(self, request):
        form = OwnerSignupForm
        return render(request, 'signup_owner.html', {'form': form})

    def post(self, request):
        form = OwnerSignupForm(request.POST)
        print('Antes del is-valid()')
        if form.is_valid():
            user = form.save()
            login(request, user)
            print(f'Usuario logueado: {user}')
            # Redirect to dashboard after sign up succesfully
            return redirect('show_workspaces')
        print(form.errors)
        return render(request, 'signup_owner.html', {'form': form})


# Login view
class UserLoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                if hasattr(user, 'is_owner') and user.is_owner:

                    return redirect('show_workspaces') # Redirect to dashboard after login succesfully

                department = user.dept
                workspace_name = department.workspace_id.name
                department_name = department.name

                if workspace_name and department_name:

                    return redirect('dashboard', workspace_name=workspace_name, department_name=department_name)

        return render(request, 'login.html', {'form': form})


# Logout view
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')  # Redirect to login after log out


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class CreateUserView(View):
    def get(self, request):
        if not request.user.is_owner:
            department = request.user.dept
            if department is None:
                messages.error(request, 'No department assigned to your account.')
                return redirect('assign_department_page')

            workspace_name = department.workspace_id.name
            department_name = department.name
            return redirect('dashboard', workspace_name=workspace_name, department_name=department_name)

        user = CustomUser.objects.get(id=request.user.id)
        form = CreateUserForm(user=user)
        return render(request, 'create_user.html', {'form': form})

    def post(self, request):
        if not request.user.is_owner:
            department = request.user.dept
            if department is None:
                return redirect('error_page')
            workspace_name = department.workspace_id.name
            department_name = department.name

            return redirect('dashboard', workspace_name=workspace_name, department_name=department_name)  # Redirect to dashboard if not owner

        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_owner = False  # Ensures that the user is not an owner
            user.save()

            department = user.dept
            workspace_name = department.workspace_id.name
            department_name = department.name

            return redirect('dashboard', workspace_name=workspace_name, department_name=department_name)
        return render(request, 'create_user.html', {'form': form})


def owner_users_view(request):
    owner = request.user
    departments_owned_by_owner = Department.objects.filter(user=owner)
    users = CustomUser.objects.filter(dept__in=departments_owned_by_owner)
    return render(request, 'show_users.html', {'users': users, 'owner': owner})


@login_required
@csrf_protect
def update_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('show_users')
    else:
        form = UpdateUserForm(instance=user)

    return render(request, 'update_user.html', {'form': form, 'user': user})

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == 'POST':
        user.delete()
        return redirect('show_users')

    return render(request, 'delete_user.html', {'user': user})


@login_required
def change_password(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            user.set_password(new_password)
            user.save()
            return redirect('update_user', user_id=user.id)  # Redirige de nuevo al perfil de usuario
    else:
        form = ChangePasswordForm()

    return render(request, 'change_password.html', {'form': form, 'user': user})


# View detail info of the user
@login_required
def view_detail_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'view_detail_user.html', {'view_detail_user': user})

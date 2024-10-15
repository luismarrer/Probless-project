from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import OwnerSignupForm, LoginForm, CreateUserForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import CustomUser


# Owner sign up view
class OwnerSignupView(View):
    def get(self, request):
        form = OwnerSignupForm
        return render(request, 'signup_owner.html', {'form': form})

    def post(self, request):
        form = OwnerSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard') # Redirect to dashboard after sign up succesfully
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
                return redirect('dashboard')  # Redirect to dashboard after login succesfully
        return render(request, 'login.html', {'form': form})

# Logout view
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')  # Redirect to login after log out


@method_decorator(login_required, name='dispatch')
class CreateUserView(View):
    def get(self, request):
        if not request.user.is_owner:
            return redirect('dashboard')  # Redirect if not owner

        form = CreateUserForm()
        return render(request, 'create_user.html', {'form': form})

    def post(self, request):
        if not request.user.is_owner:
            return redirect('dashboard')  # Redirect to dashboard if not owner

        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_owner = False  # Ensures that the user is not an owner
            user.save()

            return redirect('dashboard')
        return render(request, 'create_user.html', {'form': form})


# Dashboard view
class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard.html')

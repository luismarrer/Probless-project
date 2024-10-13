from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import OwnerSignupForm, LoginForm
# from django.contrib.auth.models import CustomUser  # Asegúrate de que este sea tu modelo de usuario

# Vista para el registro de un Owner
class OwnerSignupView(View):
    def get(self, request):
        form = OwnerSignupForm()
        return render(request, 'account/registration/signup_owner.html', {'form': form})

    def post(self, request):
        form = OwnerSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión automáticamente después de registrarse
            return redirect('dashboard')  # Redirigir al dashboard
        return render(request, 'account/registration/signup_owner.html', {'form': form})

# Vista para el inicio de sesión
class UserLoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/registration/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirigir al dashboard
        return render(request, 'account/registration/login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)  # Llamada a la función de logout de Django
        return redirect('login')  # Redirigir al login después de cerrar sesión


# Vista para el dashboard
class DashboardView(View):
    def get(self, request):
        return render(request, 'account/dashboard.html')  # Renderiza el dashboard

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def form(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente después del registro
            return redirect('home')  # Redirige a la página principal (puedes cambiar la URL)
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})
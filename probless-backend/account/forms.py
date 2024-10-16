from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from workspace.models import Department


class OwnerSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit = False)
        user.is_owner = True
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class CreateUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'role', 'dept', 'password1', 'password2']
        

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        # Filtrar departamentos por el usuario proporcionado
        if user:
            self.fields['dept'].queryset = Department.objects.filter(user=user)

        # Personalizar la forma en que los departamentos se muestran en el formulario
        self.fields['dept'].label_from_instance = self.format_department_label

    # Método para formatear la etiqueta de cada opción en el campo 'dept'
    def format_department_label(self, department):
        return f"{department.workspace_id.name} - {department.name}"

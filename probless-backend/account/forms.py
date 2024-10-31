from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from workspace.models import Department


class OwnerSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control form-control-lg'})

    def save(self, commit=True):
        user = super().save(commit = False)
        user.is_owner = True
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg'
    }))


class CreateUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'role', 'dept', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg'}),
            'role': forms.Select(attrs={'class': 'form-control form-control-lg'}),  # Select para 'role'
            'dept': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control form-control-lg'})

        if user:
            self.fields['dept'].queryset = Department.objects.filter(user=user)

        self.fields['dept'].label_from_instance = self.format_department_label


    # Método para formatear la etiqueta de cada opción en el campo 'dept'
    def format_department_label(self, department):
        return f"{department.workspace_id.name} - {department.name}"


class UpdateUserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'dept', 'role']  # All info of user except for the password
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg'}),
            'role': forms.Select(attrs={'class': 'form-control form-control-lg'}),  # Select para 'role'
            'dept': forms.Select(attrs={'class': 'form-control form-control-lg'}),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs) 
        
        if user:
            self.fields['dept'].queryset = Department.objects.filter(user=user)

        self.fields['dept'].label_from_instance = self.format_department_label
    
    def format_department_label(self, department):
        return f"{department.workspace_id.name} - {department.name}"


    def save(self, commit=True):
        return super().save(commit=commit)


class ChangePasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg'
    }))

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password and confirm_password and new_password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match.")
        return cleaned_data

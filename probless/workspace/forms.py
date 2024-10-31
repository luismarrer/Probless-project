from django import forms
from .models import Workspace, Department

class WorkspaceForm(forms.ModelForm):
	class Meta:
		model = Workspace
		fields = ['name', 'description']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
			'description': forms.Textarea(attrs={'class': 'form-control form-control-sm'}),
			}

class DepartmentForm(forms.ModelForm):
	class Meta:
		model = Department
		fields = ['name', 'description']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
			'description': forms.Textarea(attrs={'class': 'form-control form-control-sm',}),
			}


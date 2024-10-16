from django import forms
from .models import Workspace, Department

class WorkspaceForm(forms.ModelForm):
	class Meta:
		model = Workspace
		fields = ['name', 'description']

class DepartmentForm(forms.ModelForm):
	class Meta:
		model = Department
		fields = ['name', 'description']
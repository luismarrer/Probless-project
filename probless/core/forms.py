from django import forms
from .models import Ticket
from workspace.models import Department
from django_ckeditor_5.widgets import CKEditor5Widget

class TicketForm(forms.ModelForm):
    def __init__(self, *args, workspace, show_documentation=False, **kwargs):
        super().__init__(*args, **kwargs)
        if workspace:
            self.fields['assigned_department_id'].queryset = Department.objects.filter(workspace_id=workspace.id)
        if not show_documentation:
            self.fields.pop('documentation')

        self.fields['title'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['description'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['priority'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['assigned_department_id'].widget.attrs.update({'class': 'form-control form-control-lg'})

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'priority', 'assigned_department_id', 'image', 'tags', 'documentation']
        widgets = {
           "documentation": CKEditor5Widget(config_name='default')
        }

from django import forms
from .models import Ticket
from workspace.models import Department

class TicketForm(forms.ModelForm):
    def __init__(self, *args, workspace, show_documentation=False, **kwargs):
        # Llamamos al constructor de la superclase para inicializar el formulario
        super().__init__(*args, **kwargs)

        # Filtramos los departamentos según el workspace proporcionado
        if workspace:
            self.fields['assigned_department_id'].queryset = Department.objects.filter(workspace_id=workspace.id)

        # Only show documentation in the form if True
        if not show_documentation:
            self.fields.pop('documentation')


    class Meta:
        model = Ticket
        fields = ['title', 'description', 'priority', 'assigned_department_id', 'image', 'tags', 'documentation']

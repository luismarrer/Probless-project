from .models import Workspace
from django.contrib.auth.models import AnonymousUser

def ctx_dict(request):
    if isinstance(request.user, AnonymousUser) or not request.user.is_authenticated:
        return {}

    try:
        workspaces_ctx = Workspace.objects.filter(user=request.user)
        return {'workspaces_ctx': workspaces_ctx}
    except Workspace.DoesNotExist:
        # Si no existe un Workspace relacionado, puedes retornar un contexto vacío o un mensaje
        return {'workspaces_ctx': []}
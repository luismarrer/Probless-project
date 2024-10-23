from .models import Workspace
from django.contrib.auth.models import AnonymousUser

def ctx_dict(request):
    if isinstance(request.user, AnonymousUser) or not request.user.is_authenticated:
        # Si el usuario no está autenticado, retorna un contexto vacío o lo que necesites
        return {}
    workspaces_ctx = Workspace.objects.filter(user=request.user)
    ctx = {'workspaces_ctx': workspaces_ctx}
    return ctx
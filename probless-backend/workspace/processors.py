from .models import Workspace

def ctx_dict(request):
    workspaces_ctx = Workspace.objects.filter(user=request.user)
    ctx = {'workspaces_ctx': workspaces_ctx}
    return ctx 
from django.shortcuts import render
from django.views import View

# Create your views here.
def home(request):
	return render(request, 'home.html')

# Dashboard view
class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard.html')
from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, template_name="dashboard.html", context={})

from django.shortcuts import render


# Create your views here.
def generator(request):
    return render(request, template_name="generator.html", context={})


def profile(request):
    return render(request, template_name="juicy-luicy.html", context={})

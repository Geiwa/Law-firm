from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request=request, template_name='blog/index.html')


def about(request):
    return render(request=request, template_name='blog/about.html')


def service(request):
    return render(request=request, template_name='blog/service.html')


def contact(request):
    return render(request=request, template_name='blog/contact.html')

from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm


# Create your views here.


def index(request):
    return render(request=request, template_name='blog/index.html')


def about(request):
    return render(request=request, template_name='blog/about.html')


def service(request):
    return render(request=request, template_name='blog/service.html')




def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            contact = Contact(name=name, email=email, message=message)
            contact.save()
            return redirect("index")
        
    else:
        form = ContactForm()

    return render(request,  'blog/contact.html',  {'form': form})

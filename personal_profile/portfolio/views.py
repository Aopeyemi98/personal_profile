from django.shortcuts import render, redirect
from .models import Experience, Project, Contact
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect,HttpResponse
from .forms import ContactForm

def home(request):
    return render(request=request, template_name='portfolio/home.html')


def about(request):
    return render(request=request, template_name='portfolio/about.html')


def experience(request):
    exp = Experience.objects.all()
    return render(request=request, template_name='portfolio/experience.html', context={'experiences':exp})


def projects(request):
    project = Project.objects.all()
    return render(request=request, template_name='portfolio/projects.html', context={'projects':project})

def skills(request):
    return render(request=request, template_name='portfolio/skills.html')

def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        # print(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('contact/home/')
            success = {'success': 'Thank you, your message is received successfully'}
            return render(request=request, template_name='portfolio/contact.html', context=success )
    context = {'form': form}
    return render(request=request, template_name='portfolio/contact.html', context=context)


def update_contact(request, pk):
    update = Contact.objects.get(id=pk)
    update_contact_form = ContactForm(instance=update)

    context = {'form': update_contact_form}
    return render(request=request, template_name='portfolio/contact.html', context=context)


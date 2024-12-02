from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from django.views.generic import ListView, DetailView
from .models import Projects



def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')



def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form':form})




class ProjectView(ListView):
    model = Projects
    template_name = 'project/projects.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectView, self).get_context_data(*args, **kwargs)
        return context


class ProjectDetailView(DetailView):
    model = Projects
    template_name = 'project/projects_detail.html'  # Ensure this matches your template name
    context_object_name = 'project' 
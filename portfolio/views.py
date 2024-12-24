from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from.forms import ContactForm
# Create your views here.


def home_view(request):
    return render(request, 'home.html')


def about_view(request):
    return render(request, 'about.html')

def portfolio_view(request):
    return render(request, 'services.html')


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')
    

    def get_context_data(self, *args, **kwargs):
        context  =super(ContactView,self).get_context_data( *args, **kwargs)
        return context

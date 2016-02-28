from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import FormView, CreateView

from .forms import ContactForm
from .models import Message


class ContactView(CreateView):
    model = Message
    form_class = ContactForm
    template_name = 'erup/form.html'
    success_url = '?success'

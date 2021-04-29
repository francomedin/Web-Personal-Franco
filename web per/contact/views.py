
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .forms import ContactForm
from .models import Contact
# Create your views here.


class ContactCreate(CreateView):
    form_class = ContactForm
    model = Contact
    success_url = reverse_lazy('contact')

    
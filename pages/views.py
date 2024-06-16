from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView
from .forms import ContactModelForm
from django.core.mail import send_mail
from pages.models import *


class HomePageView(TemplateView):
    template_name = 'home.html'
    login_url = 'users:login'


class ContactTemplateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm
    success_url = '/'

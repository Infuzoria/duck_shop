from mailing_app.forms import ClientForm, TextForm
from mailing_app.models import Client, Text
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = '/clients'


class ClientListView(ListView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = '/clients'


class ClientDeleteView(DeleteView):
    model = Client
    success_url = '/clients'


class TextCreateView(CreateView):
    model = Text
    form_class = TextForm
    success_url = '/texts'

from mailing_app.forms import ClientForm
from mailing_app.models import Client
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

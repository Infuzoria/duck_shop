from mailing_app.forms import ClientForm, TextForm, NewsletterForm
from mailing_app.models import Client, Text, Newsletter
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


class TextListView(ListView):
    model = Text


class TextUpdateView(UpdateView):
    model = Text
    form_class = TextForm
    success_url = '/texts'


class TextDeleteView(DeleteView):
    model = Text
    success_url = '/texts'


class NewsletterCreateView(CreateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = '/newsletters'


class NewsletterListView(ListView):
    model = Newsletter


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = '/newsletters'

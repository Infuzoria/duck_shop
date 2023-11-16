from mailing_app.forms import ClientForm, TextForm, NewsletterForm
from mailing_app.models import Client, Text, Newsletter, Logs
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from mailing_app.cron import start_mailing_job
from django.shortcuts import redirect


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


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    success_url = '/newsletters'


class LogsListView(ListView):
    model = Logs

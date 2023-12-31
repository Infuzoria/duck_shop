from mailing_app.forms import ClientForm, TextForm, NewsletterForm
from mailing_app.models import Client, Text, Newsletter, Logs, User
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from mailing_app.cron import start_mailing_job
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse


class ClientCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'mailing_app.add_client'
    model = Client
    form_class = ClientForm
    success_url = '/clients'


class ClientListView(PermissionRequiredMixin, ListView):
    permission_required = 'mailing_app.view_client'
    model = Client

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner_id=self.request.user.id)
        return queryset


class ClientUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'mailing_app.change_client'
    model = Client
    form_class = ClientForm
    success_url = '/clients'


class ClientDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'mailing_app.delete_client'
    model = Client
    success_url = '/clients'


class TextCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'mailing_app.add_text'
    model = Text
    form_class = TextForm
    success_url = '/texts'


class TextListView(PermissionRequiredMixin, ListView):
    permission_required = 'mailing_app.view_text'
    model = Text

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner_id=self.request.user.id)
        return queryset


class TextUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'mailing_app.change_text'
    model = Text
    form_class = TextForm
    success_url = '/texts'


class TextDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'mailing_app.delete_text'
    model = Text
    success_url = '/texts'


class NewsletterCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'mailing_app.add_newsletter'
    model = Newsletter
    form_class = NewsletterForm
    success_url = '/newsletters'

    def get_form(self, form_class=None):
        form = super(NewsletterCreateView, self).get_form(form_class)
        form.fields['client'].queryset = Client.objects.filter(owner_id=self.request.user.id)
        form.fields['message'].queryset = Text.objects.filter(owner_id=self.request.user.id)
        form.fields['owner'].queryset = User.objects.filter(id=self.request.user.id)
        return form


class NewsletterListView(PermissionRequiredMixin,  ListView):
    permission_required = 'mailing_app.view_newsletter'
    model = Newsletter
    success_url = '/newsletters'

    def post(self, request, *args, **kwargs):
        print('Запущена ручная рассылка')
        start_mailing_job(self.request.user.id)
        return redirect(self.success_url)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_user():
            queryset = queryset.filter(owner_id=self.request.user.id)

        return queryset


class NewsletterUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'mailing_app.change_newsletter'
    model = Newsletter
    form_class = NewsletterForm
    success_url = '/newsletters'

    def get_form(self, form_class=None):
        form = super(NewsletterUpdateView, self).get_form(form_class)
        form.fields['client'].queryset = Client.objects.filter(owner_id=self.request.user.id)
        form.fields['message'].queryset = Text.objects.filter(owner_id=self.request.user.id)
        form.fields['owner'].queryset = User.objects.filter(id=self.request.user.id)
        return form


class NewsletterDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'mailing_app.delete_newsletter'
    model = Newsletter
    success_url = '/newsletters'


class LogsListView(PermissionRequiredMixin, ListView):
    permission_required = 'mailing_app.view_logs'
    model = Logs

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_user():
            queryset = queryset.filter(owner_id=self.request.user.id)

        return queryset


def toggle_activity(request, pk):
    newsletter_item = get_object_or_404(Newsletter, pk=pk)
    if newsletter_item.is_active:
        newsletter_item.is_active = False
    else:
        newsletter_item.is_active = True
    newsletter_item.save()
    return redirect(reverse('mailing_app:list_of_newsletters'))

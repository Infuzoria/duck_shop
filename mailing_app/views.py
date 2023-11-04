from mailing_app.forms import ClientForm
from mailing_app.models import Client
from django.views.generic import CreateView, ListView


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = '/clients'

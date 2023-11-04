from django.urls import path
from mailing_app.views import ClientCreateView, ClientListView

app_name = 'mailing_app'

urlpatterns = [
    #path('mailing/', index, name='base'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('clients/', ClientListView.as_view(), name="list_of_clients"),
]

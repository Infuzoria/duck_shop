from django.urls import path
from mailing_app.views import ClientCreateView, ClientListView, ClientUpdateView, ClientDeleteView

app_name = 'mailing_app'

urlpatterns = [
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('clients/', ClientListView.as_view(), name="list_of_clients"),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('delete_client/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
]

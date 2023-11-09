from django.urls import path
from mailing_app.views import (ClientCreateView, ClientListView, ClientUpdateView, ClientDeleteView, TextCreateView,
                               TextListView, TextUpdateView, TextDeleteView, NewsletterCreateView, NewsletterListView,
                               NewsletterUpdateView, NewsletterDeleteView)

app_name = 'mailing_app'

urlpatterns = [
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('clients/', ClientListView.as_view(), name="list_of_clients"),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('delete_client/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
    path('create_text/', TextCreateView.as_view(), name='create_text'),
    path('texts/', TextListView.as_view(), name="list_of_texts"),
    path('text_update/<int:pk>/', TextUpdateView.as_view(), name='update_text'),
    path('delete_text/<int:pk>/', TextDeleteView.as_view(), name='delete_text'),
    path('create_newsletter/', NewsletterCreateView.as_view(), name='create_newsletter'),
    path('newsletters/', NewsletterListView.as_view(), name="list_of_newsletters"),
    path('newsletter_update/<int:pk>/', NewsletterUpdateView.as_view(), name='update_newsletter'),
    path('delete_newsletter/<int:pk>/', NewsletterDeleteView.as_view(), name='delete_newsletter'),
]

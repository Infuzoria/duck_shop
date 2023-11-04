from django.urls import path
from mailing_app.views import index

app_name = 'mailing_app'

urlpatterns = [
    path('mailing/', index, name='base'),
]

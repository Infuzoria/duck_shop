from django.urls import path
from catalog.views import home_page


urlpatterns = [
    path('', home_page),
]

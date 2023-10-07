from django.urls import path
from catalog.views import home_page, contacts, product_page


urlpatterns = [
    path('', home_page),
    path('contacts/', contacts),
    path('product/', product_page)
]

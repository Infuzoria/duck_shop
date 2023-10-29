from django import forms
from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('date_of_creation', 'last_modified_date')

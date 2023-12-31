from django import forms
from catalog.models import Product, Version

PROHIBITED_CATEGORIES = ['казино', 'криптовалюта', 'крипта', 'баржа', 'дешево', 'бесплатно', 'обман',
                         'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('date_of_creation', 'last_modified_date')

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')

        if all(word not in cleaned_data.lower() for word in PROHIBITED_CATEGORIES):
            return cleaned_data

        else:
            raise forms.ValidationError('Это запрещенная категория, данный товар нельзя разместить на странице')

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')

        if all(word not in cleaned_data.lower() for word in PROHIBITED_CATEGORIES):
            return cleaned_data

        else:
            raise forms.ValidationError('Это запрещенная категория, данный товар нельзя разместить на странице')


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        exclude = ('is_active',)

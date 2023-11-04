import re
from django import forms
from mailing_app.models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

    def clean_email(self):
        cleaned_data = self.cleaned_data.get('email')
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if re.fullmatch(regex, cleaned_data):
            return cleaned_data
        else:
            raise forms.ValidationError('Адрес почты введен некорректно')

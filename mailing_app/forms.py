import re
from django import forms
from mailing_app.models import Client, Text

PROHIBITED_CATEGORIES = ['казино', 'криптовалюта', 'крипта', 'баржа', 'дешево', 'бесплатно', 'обман',
                         'полиция', 'радар']


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


class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = '__all__'

    def clean_topic(self):
        cleaned_data = self.cleaned_data.get('topic')

        if all(word not in cleaned_data.lower() for word in PROHIBITED_CATEGORIES):
            return cleaned_data

        else:
            raise forms.ValidationError('В теме присутствует упоминание запрещенной категории')

    def clean_text(self):
        cleaned_data = self.cleaned_data.get('text')

        if all(word not in cleaned_data.lower() for word in PROHIBITED_CATEGORIES):
            return cleaned_data

        else:
            raise forms.ValidationError('В сообщении присутствует упоминание запрещенной категории')

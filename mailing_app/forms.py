import re
from django import forms
from mailing_app.models import Client, Text, Newsletter

PROHIBITED_CATEGORIES = ['казино', 'криптовалюта', 'крипта', 'баржа', 'дешево', 'бесплатно', 'обман',
                         'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, forms.ModelForm):
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


class TextForm(StyleFormMixin, forms.ModelForm):
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


class NewsletterForm (StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Newsletter
        exclude = ('status', 'last_time')

    def clean_start_time(self):
        cleaned_data = self.cleaned_data.get('start_time')
        regex = re.compile(r'\b([01]?[0-9]|2[0-3]):[0-5][0-9]\b')

        if re.fullmatch(regex, cleaned_data):
            return cleaned_data
        else:
            raise forms.ValidationError('Формат времени должен быть следующий: чч:мм')

    def clean_stop_time(self):
        cleaned_data = self.cleaned_data.get('stop_time')
        regex = re.compile(r'\b([01]?[0-9]|2[0-3]):[0-5][0-9]\b')

        if re.fullmatch(regex, cleaned_data):
            return cleaned_data
        else:
            raise forms.ValidationError('Формат времени должен быть следующий: чч:мм')

from django import forms
from service.models import Сustomer, Letter, Message


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=250)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(max_length=250)


class СustomerForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Сustomer
        fields = ('email', 'name', 'comment')


class LetterForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Letter
        fields = ('name', 'time_on', 'time_off', 'periodicity', 'clients', 'status',)


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

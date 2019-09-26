from django import forms
from django.forms import ModelForm
from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publisher', 'price']


class UpdateAuthorForm(forms.Form):
    id = forms.IntegerField(label='Author Id')
    email = forms.EmailField(label="Email Address")

    def clean_email(self):
        value = self.cleaned_data['email']
        if '@' in value and value.endswith('.com'):
            return value
        else:
            raise forms.ValidationError("Invalid Email Address. Address must end with .com!")

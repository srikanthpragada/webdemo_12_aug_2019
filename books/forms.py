from django import forms


class UpdateAuthorForm(forms.Form):
    id = forms.IntegerField(label='Author Id')
    email = forms.EmailField(label="Email Address")

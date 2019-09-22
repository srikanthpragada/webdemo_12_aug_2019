from django import forms


class UpdateAuthorForm(forms.Form):
    id = forms.IntegerField(label='Author Id')
    email = forms.EmailField(label="Email Address")

    def clean_email(self):
        value = self.cleaned_data['email']
        if '@' in value and value.endswith('.com'):
            return value
        else:
            raise forms.ValidationError("Invalid Email Address. Address must end with .com!")

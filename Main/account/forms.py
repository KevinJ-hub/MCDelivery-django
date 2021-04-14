from django import forms


class my_registration_form(forms.Form):
    username = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
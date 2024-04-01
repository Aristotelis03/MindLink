from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser

# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password']

# Form that handle the registration of a user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customized fields
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder':'Username', 'id':'username', 'autocomplete':'off'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder':'Password','id':'password'})

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customized fields
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder':'Username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder':'Email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder':'Re-enter your password'})

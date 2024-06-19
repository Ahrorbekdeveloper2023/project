from django import forms
from shop.models import User

class UserEditForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Username"}))
    password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", "placeholder": "Password"}))
    first_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Last Name"}))
    phone_number = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Phone Number"}))
    email = forms.CharField(widget=forms.EmailInput({"class": "form-control", "placeholder": "Email"}))
    address = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Address"}))
    image = forms.ImageField(widget=forms.FileInput({"class": "form-control", "placeholder": "image"}))

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'phone_number', 'email', 'address', 'user_role', 'image')

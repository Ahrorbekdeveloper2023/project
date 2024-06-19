from django import forms
from shop.models import Books


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Books 
        fields = ['name', 'price', 'quantity', 'disckription', 'image', 'cotegory']  
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'disckription': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'cotegory': forms.Select(attrs={'class': 'form-control'}),
        }

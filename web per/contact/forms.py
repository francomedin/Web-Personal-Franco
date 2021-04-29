from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                       'placeholder': 'Escribe tu nombre'}
            ),

            'email': forms.EmailInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Escribe tu Email'}
            ),
            'content': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3,
                       'placeholder': 'Escribe tu Contenido'}
            )
        }

from django.forms import ModelForm, forms, Textarea,TextInput, EmailInput
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class':'form-group',
                'placeholder':'enter your name here...', 
                'style': 'max-width:400px;'
                }),
            'email': EmailInput(attrs={
                'class':'form-group',
                'placeholder':'enter your email here...',
                'style': 'max-width:400px;'
                }),
            'message': TextInput(attrs={
                'class':'form-group',
                'placeholder':'enter your message here...',
                
                }),
        }
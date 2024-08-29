from django import forms
from .models import ContactFormSubmission, PostFormSubmission

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormSubmission
        fields = ('name', 'email', 'phone', 'message')

class PostForm(forms.ModelForm):
    class Meta:
        model = PostFormSubmission
        fields = ('title', 'message', 'author')
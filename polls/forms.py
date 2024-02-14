from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your Name", max_length=100)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    name = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    
    
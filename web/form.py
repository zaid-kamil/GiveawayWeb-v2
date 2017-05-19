from django import forms

from web.models import Contact


class Add_Contact(forms.ModelForm):
    model = Contact
    fields = ["Name", "Email", "Location", "msg"]

    widgets = {

        "name": forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
        "e_mail": forms.EmailField(),
        "location": forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
        "msg": forms.TextInput(attrs={'class': 'mdl-textfield__input'}),

    }
    labels = {
        "Name": "Enter your Name",
        "Email": "Enter your Email",
        "Location": "Enter your Location or Address",
        "msg": "Enter your message",

    }

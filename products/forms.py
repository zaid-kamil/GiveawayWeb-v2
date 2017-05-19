from django import forms

from products.models import Product, Giveaway


class AddProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["p_name", "creator", "category", "actual_price", "quantity", "main_image", "screenshot2",
                  "screenshot3",
                  "product_file"]
        widgets = {
            "creator": forms.HiddenInput(attrs={'value': 'user.id'}),
            "p_name": forms.TextInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Enter a product name'}),
            "category": forms.TextInput(
                attrs={'class': 'mdl-textfield__input', 'placeholder': 'enter the type of Product'}),
            "main_image": forms.FileInput(
                attrs={'class': 'mdl-textfield__input', 'placeholder': 'Enter the products image'}),
            "screenshot2": forms.FileInput(
                attrs={'class': 'mdl-textfield__input', 'placeholder': 'Enter 1st screen shot of the product'}),
            "screenshot3": forms.FileInput(
                attrs={'class': 'mdl-textfield__input', 'placeholder': 'Enter 2nd screen shot of the product'}),
            "quantity": forms.NumberInput(
                attrs={'class': 'mdl-textfield__input', 'placeholder': 'Enter quantity which u want to give to user'}),
            "actual_price": forms.NumberInput(
                attrs={'class': 'mdl-textfield__input', 'placeholder': 'Enter a Price of product'}),
            "product_file": forms.FileInput(
                attrs={'class': 'mdl-textfield__input', 'placeholder': 'Enter a excutable product file'}),

        }
        labels = {
            "p_name": "product name",
            "category": "category for the product",
            "main_image": "Select featured image",
            "screenshot2": "choose a second image",
            "screenshot3": "choose a third image",
            "quantity": "Quantity of Product",
            "actual_price": "Real price of Product",
            "product_file": "Executable file of the product",
        }


class CreateGiveaway(forms.ModelForm):
    class Meta:
        model = Giveaway
        fields = ["g_name",
                  "user", "p_name", "entries", "description", "price", "ending_time", "image", ]

        widgets = {
            "user": forms.HiddenInput(),
            "g_name": forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            "p_name": forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            "entries": forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            "image": forms.FileInput(attrs={'class': 'mdl-textfield__input'}),
            "description": forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            "price": forms.NumberInput(attrs={'class': 'mdl-textfield__input'}),
            "ending_time": forms.DateInput(attrs={'class': 'mdl-textfield__input'}),
        }
        labels = {
            "g_name": "giveaway name",
            "user": "user name",
            "p_name": "enetr a product name",
            "description": "about the giveaway",
            "image": "choose a image for giveaway",
            "price": "Price of giveaway",
        }

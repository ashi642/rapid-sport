from django import forms
from .models import Order, CustomJersey


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order

        fields = [
            "customer_name",
            "phone",
            "size",
            "quantity",
            "custom_name",
            "custom_number",
            "address",
        ]

        widgets = {
            "customer_name": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Your name"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Phone number"
            }),

            "size": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Example: M"
            }),

            "quantity": forms.NumberInput(attrs={
                "class": "form-input",
                "min": 1
            }),

            "custom_name": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Optional"
            }),

            "custom_number": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Optional"
            }),

            "address": forms.Textarea(attrs={
                "class": "form-input",
                "rows": 4,
                "placeholder": "Delivery address"
            }),
        }


class CustomJerseyForm(forms.ModelForm):

    class Meta:
        model = CustomJersey

        fields = [
            "customer_name",
            "phone",
            "name_on_jersey",
            "number",
            "team",
            "size",
            "logo",
        ]

        widgets = {
            "customer_name": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Your name"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Phone number"
            }),

            "name_on_jersey": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Name on jersey"
            }),

            "number": forms.NumberInput(attrs={
                "class": "form-input",
                "placeholder": "Jersey number"
            }),

            "team": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Team name"
            }),

            "size": forms.Select(attrs={
                "class": "form-input"
            }),

            "logo": forms.ClearableFileInput(attrs={
                "class": "form-input"
            }),
        }
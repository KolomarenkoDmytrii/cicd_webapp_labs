from django import forms
from .models import Feedback, ContactInfo


class FeedbackForm(forms.ModelForm):
    """Form for saving visitors feedbacks'."""

    class Meta:
        model = Feedback
        fields = ["user_name", "text", "rating"]

        widgets = {
            "user_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "text",
                    "placeholder": "Уведіть своє ім'я",
                }
            ),
            "text": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "type": "text",
                    "placeholder": "Уведіть свій відгук тут",
                    "style": "height: 10rem",
                }
            ),
            "rating": forms.NumberInput(
                attrs={"class": "form-control", "type": "number"}
            ),
        }


class ContactForm(forms.ModelForm):
    """Form for leaving visitors' contact information."""

    class Meta:
        model = ContactInfo
        fields = ["user_name", "email", "message"]

        widgets = {
            "user_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "text",
                    "placeholder": "Уведіть своє ім'я",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "type": "email",
                    "placeholder": "Уведіть адресу своєї електронної скриньки",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "type": "text",
                    "placeholder": "Уведіть своє повідомлення",
                    "style": "height: 10rem",
                }
            ),
        }

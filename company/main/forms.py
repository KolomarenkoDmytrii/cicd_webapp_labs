from django import forms
from .models import Feedback


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

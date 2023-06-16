
from django import forms
from django.core.exceptions import ValidationError


def is_cabinet_office_email(email_address):
    if "cabinetoffice.gov.uk" not in email_address:
        raise ValidationError("Not a Cabinet Office email.")
    return True

class FeedbackForm(forms.Form):
    template_name = "feedback.html"
    email = forms.EmailField(required=False, validators=[is_cabinet_office_email])
    content = forms.TextInput()


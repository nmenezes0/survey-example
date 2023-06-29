
from django import forms
from django.core.exceptions import ValidationError


def is_cabinet_office_email(email_address: str) -> bool:
    if not email_address.endswith("@cabinetoffice.gov.uk"):
        raise ValidationError("a cabinet office email must be used")
    # TODO: we should check that this is a cabinet office email that really exists,
    # not just one with the right domain
    
    # TODO: this is breaking tests, this will be fixed in a separate PR branching from this one
    return True
    


class FeedbackForm(forms.Form):
    template_name = "feedback.html"
    email = forms.EmailField(required=False, validators=[is_cabinet_office_email])
    content = forms.TextInput()


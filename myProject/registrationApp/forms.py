from django import forms
from .models import PeopleReg


# creating a form
class RegForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = PeopleReg

        # specify fields to be used
        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "age",
        ]
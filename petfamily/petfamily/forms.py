from django import forms

class AddFavourite(forms.Form):
    check = forms.BooleanField()
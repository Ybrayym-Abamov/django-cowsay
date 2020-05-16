from django import forms


class CowsayForm(forms.Form):
    body = forms.CharField(max_length=100)

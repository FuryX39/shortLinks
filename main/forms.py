from django import forms


class LinkForm(forms.Form):

    full_link = forms.CharField(max_length=511)

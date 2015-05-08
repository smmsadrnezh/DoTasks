from django import forms


class ListForm(forms.Form):
    title = forms.CharField(required=True,max_length=200)
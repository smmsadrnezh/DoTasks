from django import forms


class ListForm(forms.Form):
    title = forms.CharField(max_length=200)
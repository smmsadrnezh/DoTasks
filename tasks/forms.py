from django import forms


class taskForm(forms.Form):
    title = forms.CharField(max_length=200)
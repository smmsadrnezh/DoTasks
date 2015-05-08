from django import forms


class taskForm(forms.Form):
    title = forms.CharField(required=True, max_length=200)
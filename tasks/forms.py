from django import forms


class TaskForm(forms.Form):
    title = forms.CharField(required=True, max_length=200)

    # class EditTaskForm(forms.Form):
    # Deletechoices = forms.MultipleChoiceField(
    #         widget  = forms.CheckboxSelectMultiple,
    #     )
    #     Donechoices = forms.MultipleChoiceField(
    #         widget  = forms.CheckboxSelectMultiple,
    #     )
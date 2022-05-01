from django import forms 


class AgendaForm(forms.Form):
    text = forms.CharField(max_length=40, 
    widget=forms.TextInput(attrs={
        'class':"form-control", 
        'placeholder':"Digite algo que vá fazer hoje e clique 'add'",
        'aria-label':"Todo",
        'aria-describedby':"add-btn"})
)

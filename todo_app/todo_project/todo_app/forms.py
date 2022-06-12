from django import forms
from .models import *

class TodoModelForm(forms.ModelForm):
    priority_choice = [
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    ]
    completed_choice = [
        ('Completed','Completed'),
        ('Pending','Pending'),
    ]
    priority = forms.ChoiceField(widget=forms.RadioSelect,choices=priority_choice)
    details = forms.TextInput()
    completed = forms.ChoiceField(choices=completed_choice)
    class Meta:
        model =  TodoModel
        fields = '__all__'    
    
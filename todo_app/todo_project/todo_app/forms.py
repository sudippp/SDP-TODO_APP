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
    task = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    details = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    priority = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=priority_choice)
    completed = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=completed_choice,label='Status')
    class Meta:
        model =  TodoModel
        fields = '__all__'    
    
class Form2(forms.Form):
    Task = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
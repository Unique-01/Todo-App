from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class TodoListForm(forms.ModelForm):
    class Meta:
        model= Todo
        fields = ['title','due_date','category']
        widgets = {'due_date':DateInput(),'title':forms.TextInput(attrs={'placeholder':'What do you have to do?'})}
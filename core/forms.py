from django import forms
import django
from .models import *
from django.contrib.auth.forms import UserCreationForm


class DateInput(forms.DateInput):
    input_type = 'date'


class TodoListForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'due_date', 'category']
        widgets = {'due_date': DateInput(), 'title': forms.TextInput(
            attrs={'placeholder': 'What do you have to do?'})}


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2',)

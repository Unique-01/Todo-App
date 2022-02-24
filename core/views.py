from django.shortcuts import render
from django.views import generic
from .models import *
from .forms import *

# Create your views here.
class TodoList(generic.FormView,generic.ListView):
    queryset = Todo.objects.all()
    form_class = TodoListForm
    success_url = '/'
    template_name = 'index.html/'

    def form_valid(self, form):
        # to save the form
        form.save()
        return super().form_valid(form)

class TodoDelete(generic.DeleteView):
    model = Todo
    success_url = '/'
    template_name = 'todo_confirm_delete.html/'
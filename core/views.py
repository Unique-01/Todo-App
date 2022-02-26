from django.shortcuts import render
from django.views import generic
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.

class TodoList(LoginRequiredMixin,generic.FormView,generic.ListView):
    queryset = Todo.objects.all()
    form_class = TodoListForm
    success_url = '/'
    template_name = 'index.html/'
    login_url = '/accounts/login/'


    def form_valid(self, form):
        form.instance.owner = self.request.user
        # to save the form
        form.save()
        return super().form_valid(form)

class TodoDelete(generic.DeleteView):
    model = Todo
    success_url = '/'
    template_name = 'todo_confirm_delete.html/'

class SignUpView(generic.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html/'
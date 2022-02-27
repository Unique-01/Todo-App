from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default='General')
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    time = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.title


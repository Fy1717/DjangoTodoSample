# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpRequest
from django.template import loader

from .models import Todo

def home(request):
    return render(request, 'home.html')

def list_todo_items(request):
    context = {'todo_list': Todo.objects.all()}
    return render(request, 'todos/todo_list.html', context)

def insert_todo_item(request):
    todo = Todo(content = request.POST['content'])
    todo.save()
    return list_todo_items(request)

def delete_todo_item(request, todo_id):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return list_todo_items(request)


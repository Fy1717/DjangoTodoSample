from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/', views.list_todo_items),
    url(r'^insert_todo/', views.insert_todo_item, name='insert_todo_item'),
    url(r'^delete_todo_item/(?P<todo_id>\d+)$', views.delete_todo_item, name='delete_todo_item')
]
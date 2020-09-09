from django.urls import path
from . import views
from task.views import *

app_name='task'

urlpatterns = [
        path('list/<int:pl>/',listview, name="Home"),
        path('add/<int:pl>/',addTodo,name="OpenTicket"),
        path('addcommant/<int:pl>/<int:pk>/',addcommant,name="AddCommant"),
        path('update/<int:pk>/<int:pl>/',update),
        path('get/<int:pl>/<int:pk>/',get),
        path('back/<int:pk>/<int:pl>/',back),
        path('edit/<int:pk>/<int:pl>/',edit),
        path('delete/<int:pk>/<int:pl>/',deletetodo),
        path('deletecommant/<int:pk>/<int:pl>/<int:com>/',deletecommant),
]

from django.urls import path
from . import views
from dashboard.views import *

app_name='dashboard'

urlpatterns = [
        path('',home, name="home"),
        path('add/',addpanel, name="AddDashboard"),
        path('setting/<int:pk>/',setting, name="ViewDashboard"),
        path('delete/<int:pk>/',delete, name="DeleteDashboard"),
        path('addmermber/<int:pk>/',addmermber, name="AddMermber"),
        path('deletemamber/<int:pk>/<int:userid>/',deletemamber, name="DeleteMamber"),
]

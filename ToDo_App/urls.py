from django.urls import path
from ToDo_App import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task', views.task, name='task'),
    path("delete/<int:id>/",views.delete,name="del")
]

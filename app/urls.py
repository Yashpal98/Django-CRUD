from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('list/', views.list, name="List"),
    path('edit/<id>', views.edit, name="Edit"),
    path('delete/<id>', views.delete, name="Delete"),
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('detail/<str:id>', views.detail, name="detail"),
    path('delete/<str:id>', views.delete, name="delete"),
]
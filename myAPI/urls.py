from django.urls import path 
from . import views 

urlpatterns = [
    path('pizza-menu', views.PizzaMenuview.as_view()), 
]

from django.shortcuts import render
from rest_framework import generics 
from .serializers  import PizzaSeralizer
from .models import Pizza
# Create your views here.
class PizzaMenuview(generics.ListCreateAPIView):
     queryset = Pizza.objects.all()
     serializer_class = PizzaSeralizer
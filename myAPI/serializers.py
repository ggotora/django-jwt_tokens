from rest_framework import serializers 
from .models import Pizza, Topping

class PizzaSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ['id', 'name', 'topping']
        deep = 1
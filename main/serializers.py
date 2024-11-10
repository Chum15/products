from rest_framework import serializers
from .models import Product


class ReviewSerializer(serializers.ModelSerializer):
    # реализуйте все поля
    class Meta:
        model = Product
        fields = ['title', 'description', 'price']
       
    


class ProductListSerializer(serializers.Serializer):
    title = serializers.CharField()  
    price = serializers.DecimalField(max_digits=10, decimal_places=2) 
    
   
        


class ProductDetailsSerializer(serializers.ModelSerializer):
    # реализуйте поля title, description, price и reviews (список отзывов к товару)
    pass

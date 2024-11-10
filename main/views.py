from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from django.http import Http404

from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer


@api_view(['GET'])
def products_list_view(request):
    products = Product.objects.all()
    ser = ReviewSerializer(products, many = True)
    """реализуйте получение всех товаров из БД
    реализуйте сериализацию полученных данных
    отдайте отсериализованные данные в Response"""
    return Response(ser.data)


class ProductDetailsView(APIView):
    
    def get(self, request, product_id):
        """реализуйте получение товара по id, если его нет, то выдайте 404
            реализуйте сериализацию полученных данных
            отдайте отсериализованные данные в Response"""
       
        product = Product.objects.filter(id = product_id)
        if not product:
            raise Http404('Not found product')
        
        else:       
            ser = ProductListSerializer(product, many = True)  
            return Response(ser.data)
        
            
        


# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """обработайте значение параметра mark и
        реализуйте получение отзывов по конкретному товару с определённой оценкой
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        pass

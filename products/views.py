from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http.response import JsonResponse
import uuid

from products.serializers import ProductSerializer
from products.models import Product

@csrf_exempt
def createProduct(request):
    if request.method == 'POST':
        productData = JSONParser().parse(request)
        productData['productCode'] = uuid.uuid4().hex[:6].upper()
        productSerialized = ProductSerializer(data=productData)
        if productSerialized.is_valid():
            productSerialized.save()
            return JsonResponse({ 'message': 'product creation successful',
                                  'status': 201
                                }, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({ 'message': 'product data is not valid',
                                  'status': 400
                                }, status=status.HTTP_400_BAD_REQUEST)

    else:
        return JsonResponse({'message': 'Bad Request - invalid request method',
                             'status': 400
                             }, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def getAllProducts(request):
    if request.method == 'GET':
        productsList = Product.objects.all()
        productsListSerialized = ProductSerializer(productsList, many=True)
        return JsonResponse({'message': 'All Products returned',
                             'data': productsListSerialized.data,
                             'status': 200
                             }, status=status.HTTP_200_OK)

    else:
        return JsonResponse({'message': 'Bad Request - Wrong request Method',
                             'status': 400
                             }, status=status.HTTP_400_BAD_REQUEST)
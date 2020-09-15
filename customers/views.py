from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
import uuid
import json

from customers.models import Customer
from customers.serializers import CustomerSerializer


@csrf_exempt
def createCustomer(request):
    if request.method == 'POST':
        customerData = JSONParser().parse(request)
        customerData['code'] = uuid.uuid4().hex[:6].upper()
        customer_serializer = CustomerSerializer(data=customerData)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse({'message': 'Customer creation successful',
                                 'status': 201
                                 }, status=status.HTTP_201_CREATED)

        return JsonResponse({'message': 'Error creating Customer',
                             'status': 500
                             }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        return JsonResponse({'message': 'Bad Request - Wrong request Method',
                             'status': 400
                             }, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def getAllCustomers(request):
    if request.method == 'GET':
        customersList = Customer.objects.all()
        print(customersList)
        customer_serializer = CustomerSerializer(customersList, many=True)
        return JsonResponse({'message': 'All Customers returned',
                             'data': customer_serializer.data,
                             'status': 200
                             }, status=status.HTTP_200_OK)

    return JsonResponse({'message': 'Bad Request - Wrong request Method',
                             'status': 400
                             }, status=status.HTTP_400_BAD_REQUEST)
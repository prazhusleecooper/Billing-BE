from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http.response import JsonResponse

from bills.serializers import BillSerializer
from bills.models import Bill


@csrf_exempt
def createBill(request):
    if request.method == 'POST':
        billData = JSONParser().parse(request)
        billData['productsList'] = str(billData['productsList'])
        billData['customer'] = str(billData['customer'])
        billData['timeOfPurchase'] = str(billData['timeOfPurchase'])
        billDataSerialized = BillSerializer(data=billData)
        if billDataSerialized.is_valid():
            billDataSerialized.save()
            return JsonResponse({ 'message': 'bill generation successful',
                                  'status': 201
                                }, status=status.HTTP_201_CREATED)

        return JsonResponse({'message': 'invalid bill Data',
                             'status': 400
                             }, status=status.HTTP_400_BAD_REQUEST)

    return JsonResponse({'message': 'Bad Request - Wrong request Method',
                             'status': 400
                        }, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def getAllBills(request):
    if request.method == 'GET':
        billData = Bill.objects.all()
        billDataSerialized = BillSerializer(billData, many=True)
        return JsonResponse({ 'message': 'All Bills returned',
                              'data': billDataSerialized,
                              'status': 200,
                            }, status=status.HTTP_200_OK)

    return JsonResponse({'message': 'Bad Request - Wrong request Method',
                         'status': 400
                         }, status=status.HTTP_400_BAD_REQUEST)
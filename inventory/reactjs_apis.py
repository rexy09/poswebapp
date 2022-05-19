from os import name
from urllib import response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import *
from .serializers import *
import requests
import json


@api_view(['GET', ])
# @permission_classes([IsAuthenticated])
def get_product_categories(request):
    if request.method == "GET":

        product_category_qs = ProductCategory.objects.all()

        product_categories = ProductCategorySerializer(
            product_category_qs, many=True).data

        return Response(product_categories)
    else:
        return Response([])


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def add_product_category(request):
    if request.method == "POST":
        data = request.data
        
        try:
            ProductCategory.objects.create(
                name=data['name'])
            response = {'status': 'sucess'}
        except:
            response = {'status': 'error'}

        return Response(response)
    else:
        response = {}
        return Response(response)


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def edit_product_category(request):
    if request.method == "POST":
        data = request.data
        
        try:
            product_category = ProductCategory.objects.filter(
                id=data['id']).first()
            product_category.name = data['name']
            product_category.save()
            response = {'status': 'sucess'}
        except:
            response = {'status': 'error'}

        return Response(response)
    else:
        response = {}
        return Response(response)


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def delete_product_category(request):
    if request.method == "POST":
        data = request.data

        try:
            product_category = ProductCategory.objects.filter(
                id=data['id']).first()
            product_category.delete()
            response = {'status': 'sucess'}
        except:
            response = {'status': 'error'}

        return Response(response)
    else:
        response = {}
        return Response(response)


@api_view(['GET', ])
# @permission_classes([IsAuthenticated])
def get_products(request):
    if request.method == "GET":
        # _start = int(request.GET.get('_start'))
        # _limit = int(request.GET.get('_limit'))
        # product_qs = Product.objects.filter().all()[_start:_limit]
        
        product_qs = Product.objects.filter().all()

        products = ProductSerializer(
            product_qs, many=True).data

        return Response(products)
    else:
        return Response([])


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def add_product(request):
    if request.method == "POST":
        data = json.loads(request.data)

        product = Product.objects.create(
            category__id=data['category'], name=data['name'],
            barcode=data['barcode'], brand=data['brand'],
            specification=data['specification'], description=data['description'],
            stocked=data['stocked'], min_quantity=data['min_quantity'],
            wholesale_price=data['wholesale_price'], retail_price=data['retail_price'],
            image=data['image'], supplier=data['supplier'],
            )

        res = {'sucess': True}
        response = json.dumps(res)
        return Response(response)
    else:
        res = {'sucess': False}
        response = json.dumps(res)
        return Response(response)


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def edit_product(request):
    if request.method == "POST":
        data = json.loads(request.data)

        product = Product.objects.filter(id=data['id']).update(
            category__id=data['category'], name=data['name'],
            barcode=data['barcode'], brand=data['brand'],
            specification=data['specification'], description=data['description'],
            stocked=data['stocked'], min_quantity=data['min_quantity'],
            wholesale_price=data['wholesale_price'], retail_price=data['retail_price'],
            image=data['image'], supplier=data['supplier'],
        )

        res = {'sucess': True}
        response = json.dumps(res)
        return Response(response)
    else:
        res = {'sucess': False}
        response = json.dumps(res)
        return Response(response)


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def delete_product(request):
    if request.method == "POST":
        data = json.loads(request.data)

        product = Product.objects.filter(id=data['id']).delete()

        res = {'sucess': True}
        response = json.dumps(res)
        return Response(response)
    else:
        res = {'sucess': False}
        response = json.dumps(res)
        return Response(response)

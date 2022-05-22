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
        data = request.data
        
        try:
            product=Product.objects.create(
                category__id=data['category'], name=data['name'],
                barcode=data['barcode'], brand=data['brand'],
                specification=data['specification'], description=data['description'],
                min_quantity=data['min_quantity'],
                wholesale_price=data['wholesale_price'], retail_price=data['retail_price'],
                image=data['image']
            )
            for image in data['product_images']:
                image = ProductImage.objects.create(product=product,
                                                    image=image['image'])
            response = {'status': 'sucess'}
        except:
            response = {'status': 'error'}

        return Response(response)
    else:
        response = {}
        return Response(response)


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def edit_product(request):
    if request.method == "POST":
        data = request.data

        try:
            Product.objects.filter(id=data['id']).update(
                category__id=data['category'], name=data['name'],
                barcode=data['barcode'], brand=data['brand'],
                specification=data['specification'], description=data['description'],
                stocked=data['stocked'], min_quantity=data['min_quantity'],
                wholesale_price=data['wholesale_price'], retail_price=data['retail_price'],
                image=data['image']
            )

            response = {'status': 'sucess'}
        except:
            response = {'status': 'error'}
        
        return Response(response)
    else:
        response = {}
        return Response(response)


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def delete_product(request):
    if request.method == "POST":
        data = request.data

        try:
            product = Product.objects.filter(
                id=data['id']).first()
            product.delete()
            response = {'status': 'sucess'}
        except:
            response = {'status': 'error'}

        return Response(response)
    else:
        response = {}
        return Response(response)


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def add_product_images(request):
    if request.method == "POST":
        data = request.data

        try:
            product = Product.objects.filter(
                id=data['product']).first()
            for image in data['product_images']:
                image = ProductImage.objects.create(product=product,
                                                    image=image['image'])
            response = {'status': 'sucess'}
        except:
            response = {'status': 'error'}

        return Response(response)
    else:
        response = {}
        return Response(response)
    
    
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def delete_product_images(request):
    if request.method == "POST":
        data = request.data           

        try:
            for image in data['product_images']:
                image = ProductImage.objects.filter(product__id=image['product'],
                    id=image['id']).first()
                image.image.delete()
                image.delete()
            response = {'status': 'sucess'}
        except:
            response = {'status': 'error'}

        return Response(response)
    else:
        response = {}
        return Response(response)

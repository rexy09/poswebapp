from rest_framework import serializers
from .models import *



class ProductCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductCategory
        fields = ['id', 'name', ]


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ['id',  'product', 'image', ]


class ProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)
    # image = serializers.URLField(source="get_image_url", read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'barcode', 'brand', 'specification', 'description',
                  'stocked', 'min_quantity', 'wholesale_price', 'retail_price', 'image',  'product_images']




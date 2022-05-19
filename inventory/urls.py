from django.urls import path
from . import reactjs_apis

app_name = 'inventory'

urlpatterns = [
    # reactjs_apis
    path("get/product/categories", reactjs_apis.get_product_categories,
         name="get_product_categories"),
    path("add/product/category", reactjs_apis.add_product_category,
         name="add_product_category"),
    path("get/products", reactjs_apis.get_products,
         name="get_products"),
]

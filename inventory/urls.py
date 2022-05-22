from django.urls import path
from . import reactjs_apis

app_name = 'inventory'

urlpatterns = [
    # reactjs_apis
    path("get/product/categories", reactjs_apis.get_product_categories,
         name="get_product_categories"),
    path("add/product/category", reactjs_apis.add_product_category,
         name="add_product_category"),
    path("edit/product/category", reactjs_apis.edit_product_category,
         name="edit_product_category"),
    path("delete/product/category", reactjs_apis.delete_product_category,
         name="delete_product_category"),
    path("get/products", reactjs_apis.get_products,
         name="get_products"),
    path("add/product", reactjs_apis.add_product,
         name="add_product"),
    path("edit/product", reactjs_apis.edit_product,
         name="edit_product"),
    path("delete/product", reactjs_apis.delete_product,
         name="delete_product"),
    path("add/product/images", reactjs_apis.add_product_images,
         name="add_product_images"),
    path("delete/product/images", reactjs_apis.delete_product_images,
         name="delete_product_images"),
]

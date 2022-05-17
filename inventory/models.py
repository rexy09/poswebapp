from django.db import models
# from django.contrib.auth.models import User
from django.db.models import Avg, F, FloatField, Sum
# from django.urls import reverse


# Create your models here.

class ProductCategory(models.Model):
	name = models.CharField(max_length=100,)
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Product Category"
		verbose_name_plural = "Product Categories"

	def __str__(self):
		return self.name

	# def get_absolute_url(self):
	#     return reverse("ProductCategory_detail", kwargs={"pk": self.pk})


class Product(models.Model):
	category = models.ForeignKey(
		ProductCategory, related_name="product_category", on_delete=models.SET_NULL,blank=True, null=True)
	name = models.CharField(max_length=256)
	barcode = models.CharField(max_length=100,)
	brand = models.CharField(max_length=100)
	specification = models.TextField()
	description = models.TextField()
	stocked = models.BooleanField(default=False)
	min_quantity = models.PositiveIntegerField(default=0)
	wholesale_price = models.DecimalField(
		max_digits=19, decimal_places=2, default=0)
	retail_price = models.DecimalField(
		max_digits=19, decimal_places=2, default=0)
	image = models.ImageField(upload_to='products')
	supplier = models.CharField(max_length=100)
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	# @property
	# def average_cost(self):
	# 	return self.inventory_product.filter(exist=True).aggregate(product_cost=Avg('product_cost'))

	@property
	def quantity(self):
		try:
			available = self.inventory_product.filter(exist=True).aggregate(remain=Sum('remain'))[
			'remain'] - self.inventory_product.filter(exist=True).aggregate(damage=Sum('damage'))['damage']
		except:
			available = 0
		return available

	@property
	def net_worth(self):
		try:
			available = self.inventory_product.filter(exist=True).aggregate(remain=Sum('remain'))[
			'remain'] - self.inventory_product.filter(exist=True).aggregate(damage=Sum('damage'))['damage']
			worth = available * self.sell_price
		except:
			worth = 0
		return worth

	# def get_absolute_url(self):
	# 	return reverse("business:stock_list", kwargs={"id": self.business.id})

	class Meta:
		ordering = ["name"]
		verbose_name = 'Product'
		verbose_name_plural = 'Products'


class ProductImage(models.Model):
	product = models.ForeignKey(Product, related_name='product_images',
								on_delete=models.CASCADE)
	image = models.ImageField(upload_to='products')
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)

	@property
	def image_url(self):
		return "{0}".format(self.image.url)

	class Meta:
		verbose_name = "Product Image"
		verbose_name_plural = "Product Images"

	def __str__(self):
		return self.product.name

	# def get_absolute_url(self):
	#     return reverse("BoatImage_detail", kwargs={"pk": self.pk})


class Inventory(models.Model):
	product = models.ForeignKey(
		Product, related_name="inventory_product", on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField()
	remain = models.PositiveIntegerField()
	damage = models.PositiveIntegerField(default=0)
	product_cost = models.DecimalField(max_digits=19, decimal_places=2)
	exist = models.BooleanField(default=True)
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)

	# def __str__(self):
	# 	available = self.remain - self.damage
	# 	return "Product: {0}, Avaible: {1}, Cost: {2} {4}, Sell: {3} {4}".format(self.product.name, available, self.product_cost, self.product.sell_price,  self.currency)

	# @property
	# def cogs(self):
	# 	try:
	# 		amount = ((self.product_cost * self.quantity)*(self.quantity + self.damage))/(self.quantity - self.remain)
	# 	except:
	# 		amount = 0

	# 	return amount

	# @property
	# def get_available(self):
	# 	available = self.remain - self.damage
	# 	return available

	class Meta:
		verbose_name = 'Inventory'
		verbose_name_plural = 'Inventories'

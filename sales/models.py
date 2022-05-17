from django.db import models

# Create your models here.


class Customer(models.Model):

	CATEGORY = [
		('Loyal', 'Loyal'),
		('Normal', 'Normal'),
	]

	GENDER = (
		('M', 'Male'),
		('F', 'Female'),
	)

	# business = models.ForeignKey(Business, related_name="customer", on_delete=models.CASCADE)
	full_name = models.CharField(max_length=100)
	company = models.CharField(max_length=100, blank=True, null=True)
	phone = models.CharField(max_length=15, help_text="+255 format")
	gender = models.CharField(max_length=10, choices=GENDER)
	email = models.EmailField(max_length=254, blank=True, null=True)
	address = models.CharField(max_length=254)
	category = models.CharField(
		choices=CATEGORY, default=CATEGORY[1][0], max_length=20)
	points = models.PositiveIntegerField(default=0)
	country = models.CharField(max_length=100, blank=True, null=True)
	city = models.CharField(max_length=100, blank=True, null=True)
	state = models.CharField(max_length=100, blank=True, null=True)
	postal_code = models.CharField(max_length=50, blank=True, null=True)
	comments = models.TextField(blank=True, null=True)
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{0} ({1})".format(self.full_name, self.phone)

	class Meta:
		verbose_name = 'Customer'
		verbose_name_plural = 'Customers'

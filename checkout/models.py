from django.db import models
from products.models import Product


class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    house_number = models.CharField(max_length=20, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    city = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    post_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=40, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product,on_delete=models.CASCADE , null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.name, self.product.price)

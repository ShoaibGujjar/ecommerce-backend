from asyncio.windows_events import NULL
from email.policy import default
from trace import Trace
from django.forms import FileField
from djongo import models
from django.contrib.auth.models import User
from django_enumfield import enum

# Create your models here.
class Status(enum.Enum):
    PENDING = 0
    PLASED = 1
    CONFORMED = 2
    DISPATCH = 3

class Product(models.Model):
    is_active = models.BooleanField(default=True)
    product_id=models.CharField(primary_key=True,max_length=20,null=False)
    name = models.CharField(max_length=100,null=False)
    description=models.TextField(max_length=150)
    price=models.DecimalField(max_digits=7,decimal_places=2,null=False)
    priceMetal = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    countInStock=models.PositiveIntegerField(default=0)
    is_horizontal =models.BooleanField(default=False)
    def __str__(self):
        return f"{self.name}"

class Image(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE,related_name='image')
    image=models.FileField(upload_to='media',null=False)
    
    def __str__(self):
        return f"{self.image}"



class Journey(models.Model):
    title=models.CharField(max_length=150,null=True)
    description=models.TextField(max_length=300,default=NULL)
    def __str__(self):
        return f"{self.title}"

class JourneyImage(models.Model):
    Journey=models.ForeignKey(Journey, on_delete=models.CASCADE,related_name='image')
    image=models.FileField(upload_to='media',null=False)

class Story(models.Model):
    journey=models.ForeignKey(Journey, on_delete=models.CASCADE,related_name='journey')
    image=models.FileField(upload_to='media',null=False)
    description=models.TextField(max_length=1000)
    def __str__(self):
        return f"{self.description}"

class About(models.Model):
    title=models.CharField(max_length=150,null=True)
    image=models.FileField(upload_to='media',null=False)
    description=models.TextField(max_length=300)
    def __str__(self):
        return f"{self.title}"

class OrderSummary(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=100,null=False)
    email=models.EmailField(max_length=100,null=True)
    phone=models.CharField(max_length=20)
    postal_code=models.CharField(max_length=20)
    address=models.TextField(max_length=150)
    status=enum.EnumField(Status, default=Status.PENDING)
    totalAmount=models.DecimalField(null= True,max_digits=9,decimal_places=2)
    def __str__(self):
        return f"{self.name}"
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(OrderSummary, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.name)





   
class Request(models.Model):
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name=models.CharField(max_length=100,null=False)
    last_name=models.CharField(max_length=100,null=False)
    email=models.EmailField(max_length=100,null=True)
    phone=models.CharField(max_length=20)
    story=models.TextField(max_length=1000)
    def __str__(self):
        return f"{self.email}"

from django.contrib import admin
from .models import Product,OrderSummary,Image,About,Journey,Story,OrderItem

# Register your models here.
admin.site.register(Image)
admin.site.register(Product)
admin.site.register(OrderSummary)
admin.site.register(About)
admin.site.register(Journey)
admin.site.register(Story)
admin.site.register(OrderItem)



from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User


from . import models


class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Image
        fields='__all__'

class DetailImageSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Image
        fields=['image']

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Product
        fields='__all__'

class DetailProductSerializers(serializers.ModelSerializer):
    image=DetailImageSerializers(many=True)
    class Meta:
        model=models.Product
        fields=['product_id','name','description','image','price','is_horizontal']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = '__all__'
        
    
class OrderSummarySerializers(serializers.ModelSerializer):
    orderitems = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=models.OrderSummary
        fields='__all__'
    def get_orderitems(self, obj):
        orderitems = obj.orderitem_set.all()
        serializer = OrderItemSerializer(orderitems, many=True)
        return serializer.data

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.OrderSummary
        fields='__all__'

class JourneySerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Journey
        fields='__all__'

class ImageJourneySerializers(serializers.ModelSerializer):
    class Meta:
        model=models.JourneyImage
        fields='__all__'

class StorySerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Story
        fields='__all__'

class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.About
        fields='__all__'

class RequestSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Request
        fields='__all__'
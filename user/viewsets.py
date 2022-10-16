from itertools import product
from rest_framework import viewsets,mixins
from .models import Product,Request
from .serializers import ProductSerializers,DetailProductSerializers,RequestSerializers

class DetailProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=DetailProductSerializers
    lookup_field='pk'

class RequestViewSet(viewsets.ModelViewSet):
    queryset=Request.objects.all()
    serializer_class=RequestSerializers
    lookup_field='pk'
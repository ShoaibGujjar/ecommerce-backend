from itertools import product
from rest_framework import viewsets,mixins,generics
from user.models import About, Journey, Product,OrderSummary,Image, Story,JourneyImage
from user.serializers import OrderSerializers,AboutSerializers, JourneySerializers, ImageJourneySerializers,ProductSerializers,OrderSummarySerializers,ImageSerializers, StorySerializers

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
    lookup_field='pk'

class OrderSummaryViewSet(viewsets.ModelViewSet):
    queryset=OrderSummary.objects.all()
    serializer_class=OrderSummarySerializers
    lookup_field='pk'

class OrderViewSet(viewsets.ModelViewSet):
    queryset=OrderSummary.objects.all()
    serializer_class=OrderSerializers
    lookup_field='pk'

class ImageViewSet(viewsets.ModelViewSet):
    queryset=Image.objects.all()
    serializer_class=ImageSerializers
    lookup_field='pk'

class JourneyViewSet(viewsets.ModelViewSet):
    queryset=Journey.objects.all()
    serializer_class=JourneySerializers
    lookup_field='pk'

class JourneyImageViewSet(viewsets.ModelViewSet):
    queryset=JourneyImage.objects.all()
    serializer_class=ImageJourneySerializers
    lookup_field='pk'

class StoryViewSet(viewsets.ModelViewSet):
    queryset=Story.objects.all()
    serializer_class=StorySerializers
    lookup_field='pk'

class AboutViewSet(viewsets.ModelViewSet):
    queryset=About.objects.all()
    serializer_class=AboutSerializers
    lookup_field='pk'

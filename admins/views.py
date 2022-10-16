from re import I
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import BasePermission,IsAuthenticated, IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializer, UserSerializerWithToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status,generics,mixins
from django.shortcuts import get_object_or_404

from user.models import About, Journey, Product,OrderSummary,Image, Story
from user.serializers import OrderSerializers,ProductSerializers,OrderSummarySerializers,ImageSerializers,JourneySerializers,AboutSerializers, StorySerializers

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def registerUser(request):
    data = request.data
    if(data['email'] != '' and data['password'] != ''):
        try:
            user = User.objects.create(
                first_name=data['name'],
                username=data['email'],
                email=data['email'],
                password=make_password(data['password'])
            )
            # message = {'detail': 'user created'}
            serializer = UserSerializerWithToken(user, many=False)
            return Response(serializer.data)
        except:
            message = {'detail': 'already exist'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    else:
        message = {'detail': 'information is not correct'}
    return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    user = request.user
    serializer = UserSerializerWithToken(user, many=False)

    data = request.data
    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']
    if data['password'] != '':
        user.password = make_password(data['password'])

    user.save()

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
    lookup_field='pk'
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

class productUpdateAPIView(generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
    lookup_field = 'pk'
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class OrderUpdateAPIView(generics.UpdateAPIView):
    queryset=OrderSummary.objects.all()
    serializer_class=OrderSummarySerializers
    lookup_field = 'pk'
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class OrderDestroyAPIView(generics.DestroyAPIView):
    queryset=OrderSummary.objects.all()
    serializer_class=OrderSummarySerializers
    lookup_field='pk'
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

class ImageUpdateAPIView(generics.UpdateAPIView):
    queryset=Image.objects.all()
    serializer_class=ImageSerializers
    lookup_field = 'pk'
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class ImageDestroyAPIView(generics.DestroyAPIView):
    queryset=Image.objects.all()
    serializer_class=ImageSerializers
    lookup_field='pk'
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


class JournyUpdateAPIView(generics.UpdateAPIView):
    queryset=Journey.objects.all()
    serializer_class=JourneySerializers
    lookup_field = 'pk'
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class JourneyDestroyAPIView(generics.DestroyAPIView):
    queryset=Journey.objects.all()
    serializer_class=JourneySerializers
    lookup_field='pk'
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

class AboutUpdateAPIView(generics.UpdateAPIView):
    queryset=About.objects.all()
    serializer_class=AboutSerializers
    lookup_field = 'pk'
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class AboutDestroyAPIView(generics.DestroyAPIView):
    queryset=About.objects.all()
    serializer_class=AboutSerializers
    lookup_field='pk'
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

class StoryUpdateAPIView(generics.UpdateAPIView):
    queryset=Story.objects.all()
    serializer_class=StorySerializers
    lookup_field = 'pk'
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class StoryDestroyAPIView(generics.DestroyAPIView):
    queryset=Story.objects.all()
    serializer_class=StorySerializers
    lookup_field='pk'
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)



# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getOrderById(request, pk):
#     try:
#         user = request.user
#         order = OrderSummary.objects.get(id=pk)
#         if user.is_staff or order.user == user:
#             serializer = OrderSerializer(order, many=False)
#             return Response(serializer.data)
#         else:
#             Response({'detail': 'Not authorized to view this order'},
#                      status=status.HTTP_400_BAD_REQUEST)
#     except:
#         return Response({'detail': 'Order does nort exists'},
#                         status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getMyOrder(request,pk):
    user = User.objects.get(id=pk)
    queryset=OrderSummary.objects.filter(user=user)
    serializer = OrderSummarySerializers(queryset, many=True)
    return Response(serializer.data)





@api_view(['POST'])
def userMixinView(request):
    data=request.data
    image = data['image']
    serializer=ProductSerializers(data=request.data)
    product = Product.objects.create(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            countInStock=data['countInStock'],
            is_horizontal=data['is_horizontal']
        )
    for i in image:
        item = Image.objects.create(
            product=product,
            image=i['image']
            )
    obj=Product.objects.get(product_id=product)
    data=ProductSerializers(obj,many=False).data
    return Response(data)


@api_view(['POST'])
def userMixinView(request):
    data=request.data
    image = data['image']
    serializer=ProductSerializers(data=request.data)
    product = Product.objects.create(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            countInStock=data['countInStock'],
            is_horizontal=data['is_horizontal']
        )
    for i in image:
        item = Image.objects.create(
            product=product,
            image=i['image']
            )
    obj=Product.objects.get(product_id=product)
    data=ProductSerializers(obj,many=False).data
    return Response(data)


@api_view(['UPDATE'])
def updateView(request,pk):
    data=request.data
    product = Product.objects.get(product_id=data['product_id'])
    product.name=data['name'],
    product.description=data['description'],
    product.price=data['price'],
    product.countInStock=data['countInStock'],
    product.is_horizontal=data['is_horizontal']
    product.save()

    image1 = Image.objects.get(id=data['id1'])
    image1.image=data['image1'],
    image1.save()


    image2 = Image.objects.get(id=data['id2'])
    image2.image=data['image2'],
    image2.save()

    image3 = Image.objects.get(id=data['id3'])
    image3.image=data['image3'],
    image3.save()
    
    image4= Image.objects.get(id=data['id4'])
    image4.image=data['image4'],
    image4.save()
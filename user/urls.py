from django.urls import path
from . import views
from rest_framework.permissions import AllowAny

urlpatterns = [
    path('order/',views.orderListCreateAPIView.as_view(permission_classes=[AllowAny]),name='addorder',), 
    path('relatedproduct/',views.RelatedProductAPIView),    
    path('sendmail/',views.SendDynamic),
    path('changeorderstatus/',views.ChangeOrderStatus) ,
    path('addOrderItems/',views.addOrderItems,name='addOrderItems',),  
]
from django.urls import path
from rest_framework.permissions import AllowAny

from . import views

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.registerUser, name="register"),
    path('profile/', views.getUserProfile, name="users-profile"),
    path('profile/update/', views.updateUserProfile, name="users-profile-update"),
    path('', views.getUsers, name="users"),
    path('myorders/<str:pk>/', views.getMyOrder, name='myorder'),
    # path('<str:pk>/', views.getOrderById, name='user-order'),
    path('addproduct/',views.userMixinView,name='addproduct',),
    path('destroyproduct/<str:pk>/',views.ProductDestroyAPIView.as_view(),name='destroyproduct',),
    path('destroyorder/<int:pk>/',views.OrderDestroyAPIView.as_view()),
    path('destroyimage/<int:pk>/',views.ImageDestroyAPIView.as_view()),
    path('destroyabout/<int:pk>/',views.AboutDestroyAPIView.as_view()),
    path('destroystory/<int:pk>/',views.StoryDestroyAPIView.as_view()),
    path('updateproduct/<str:pk>/',views.productUpdateAPIView.as_view(),name='updateproduct',),
    path('updateorder/<int:pk>/',views.OrderUpdateAPIView.as_view(),name='updateflavour',),
    path('updateimage/<int:pk>/',views.ImageUpdateAPIView.as_view(),name='updatezipcode',),
    path('updateabout/<int:pk>/',views.AboutUpdateAPIView.as_view(),name='updateabout',),
    path('updatestory/<int:pk>/',views.StoryUpdateAPIView.as_view(),name='updatestory',),

]
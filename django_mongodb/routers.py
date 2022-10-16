
from rest_framework.routers import DefaultRouter

from admins.viewsets import OrderViewSet,ProductViewSet,OrderSummaryViewSet,ImageViewSet,StoryViewSet,AboutViewSet,JourneyViewSet
from user.viewsets import DetailProductViewSet,RequestViewSet

router=DefaultRouter()
router.register('products',ProductViewSet,basename='products')
router.register('orderdetail',OrderSummaryViewSet,basename='orderdetail')
router.register('order',OrderViewSet,basename='order')
router.register('image',ImageViewSet,basename='image')
router.register('story',StoryViewSet,basename='story')
router.register('journey',AboutViewSet,basename='journey')
router.register('about',JourneyViewSet,basename='about')

router.register('detailproduct',DetailProductViewSet,basename='detailproduct')
router.register('request',RequestViewSet,basename='request')
urlpatterns=router.urls


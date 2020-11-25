from myproject.viewsets import CarViewset, UserViewset, OfferViewset, MessageViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('car',CarViewset)
router.register('user',UserViewset)
router.register('offer',OfferViewset)
router.register('message',MessageViewset)
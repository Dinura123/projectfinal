from myproject.viewsets import CarViewset
from myproject.viewsets import UserViewset
from myproject.viewsets import OfferViewset
from myproject.viewsets import ReservationViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('car',CarViewset)
router.register('user',UserViewset)
router.register('offer',OfferViewset)
router.register('reservation',ReservationViewset)
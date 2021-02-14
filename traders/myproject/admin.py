from django.contrib import admin
from myproject.models import Car
#from myproject.models import User
from myproject.models import Offer
from myproject.models import Reservation
# Register your models here.

admin.site.register(Car)
#admin.site.register(User)
admin.site.register(Offer)
admin.site.register(Reservation)
from django.contrib import admin

from .models import Merchant,Area,PriceByAreaAndUnit,Parcel,ParcelDetails
# Register your models here.

admin.site.register(Merchant)
admin.site.register(Area)
admin.site.register(PriceByAreaAndUnit)
admin.site.register(Parcel)
admin.site.register(ParcelDetails)

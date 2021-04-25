from rest_framework import serializers
from .models import Merchant,Area,PriceByAreaAndUnit,Parcel,ParcelDetails



class PriceByAreaAndUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model=PriceByAreaAndUnit
        fields=('id','quantity_price_title','price')



class AreaWiseUnitPriceSerializer(serializers.ModelSerializer):
    price_by_area_unit=PriceByAreaAndUnitSerializer(many=True, read_only=True)
    
    #added_on=serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model=Area
        fields=('id','title','cod_charge_percentage','return_charge_percentage','price_by_area_unit')


from django.db import models

# Create your models here.

class Merchant(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Area(models.Model):
    title=models.CharField(max_length=200)
    cod_charge_percentage=models.FloatField(default=0)
    return_charge_percentage=models.FloatField(default=0)

    def __str__(self):
        return self.title


class PriceByAreaAndUnit(models.Model):
    area=models.ForeignKey(Area, related_name='price_by_area_unit',on_delete=models.CASCADE)
    quantity_price_title=models.CharField(max_length=50)
    price=models.FloatField(default=0)

    def __str__(self):
        return self.area.title + ' - ' + self.quantity_price_title+' '+str(self.price)


PRODUCT_TYPES = (
('fragile','Fragile'),
('liquid','Liquid'),
)
 
class Parcel(models.Model):
    merchant=models.ForeignKey(Merchant, related_name='parcel',on_delete=models.CASCADE)
    merchant_invoice_id=models.CharField(max_length=4)
    product_type=models.CharField(max_length=10,choices=PRODUCT_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def price(self):
        area=self.parcel_details.price_by_area_and_unit.area
        base_price=self.parcel_details.price_by_area_and_unit.price
        total=base_price+base_price*(area.cod_charge_percentage/100)+base_price*(area.return_charge_percentage/100)
        
        return round(total,2)

    def area(self):
        return self.parcel_details.price_by_area_and_unit.area.title

    def unit_and_price(self):
        
        return self.parcel_details.price_by_area_and_unit.quantity_price_title


    def __str__(self):
        try:
            return 'Merchant Invoice ID: '+self.merchant_invoice_id+' - '+'Total: '+str(self.price())
        except:
            return 'Merchant Invoice ID: '+self.merchant_invoice_id
            

class ParcelDetails(models.Model):
    parcel=models.OneToOneField(Parcel,related_name='parcel_details',on_delete=models.CASCADE)
    price_by_area_and_unit=models.ForeignKey(PriceByAreaAndUnit, related_name='parcel_details',on_delete=models.CASCADE)


    def __str__(self):

        return 'Merchant Invoice ID: '+self.parcel.merchant_invoice_id






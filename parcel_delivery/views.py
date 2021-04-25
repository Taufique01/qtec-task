from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer

from .models import Merchant,Area,PriceByAreaAndUnit,Parcel,ParcelDetails
from .serializers import AreaWiseUnitPriceSerializer,PriceByAreaAndUnitSerializer


class ParcelListView(LoginRequiredMixin,APIView):
     
      renderer_classes = [TemplateHTMLRenderer]
      template_name = 'parcel_list.html'
      

      def get(self, request, *args, **kwargs):

         parcelList=Parcel.objects.all()

          
          

         return Response({'parcelList':parcelList})




class AddParcelView(LoginRequiredMixin,APIView):
     
      renderer_classes = [TemplateHTMLRenderer]
      template_name = 'add_parcel.html'
      

      def get(self, request, *args, **kwargs):

          merchants=Merchant.objects.all()
          areas=Area.objects.all()
          return Response({'merchants':merchants,'areas':areas})


      def post(self, request, *args, **kwargs):



         try:

            parcel=Parcel()
            parcel.merchant=Merchant.objects.get(id=request.data['merchant_id'])
            parcel.merchant_invoice_id=request.data['invoice_id']
            parcel.product_type=request.data['product_type']
            parcel.save()
            
            
            parcel_details=ParcelDetails()
            parcel_details.parcel=parcel
            parcel_details.price_by_area_and_unit=PriceByAreaAndUnit.objects.get(id=request.data['price_option_id'])
            parcel_details.save()
            message='Data saved successful'


         except Exception as e:
             message='Error while saving data'
             print(e)
            



         print(request.data)
         merchants=Merchant.objects.all()
         areas=Area.objects.all()

          
          

         return Response({'merchants':merchants,'areas':areas,'message':message})

    


class AreaWiseUnitPriceView(LoginRequiredMixin,APIView):
     
      def get(self, request, *args, **kwargs):


          areas=Area.objects.all()
          serializer=AreaWiseUnitPriceSerializer(areas, many=True)
          #print(serializer.data)

          return Response({'area_wise_unit_price':serializer.data})




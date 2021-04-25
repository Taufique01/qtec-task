from django.urls import path,re_path
from .views import AddParcelView,AreaWiseUnitPriceView,ParcelListView
urlpatterns = [
    path('',ParcelListView.as_view(),name='parcel_list'),
    path('add-parcel',AddParcelView.as_view(),name='add_parcel'),
    path('fetch-area-wise-unit-price',AreaWiseUnitPriceView.as_view(),name='fetch_area_wise_unit_price'),


   
]

var AREA={};

$.ajax({
    url: "/fetch-area-wise-unit-price",
    success: function (data) { 

        console.log(data.area_wise_unit_price);
        var area_wise_unit_price=data.area_wise_unit_price;
       
        for(var i=0;i<area_wise_unit_price.length;i++){
            AREA[area_wise_unit_price[i].id]=area_wise_unit_price[i];

            var price_by_area_unit={};

            for(var j=0;j<area_wise_unit_price[i].price_by_area_unit.length;j++){
                price_by_area_unit[area_wise_unit_price[i].price_by_area_unit[j].id]=area_wise_unit_price[i].price_by_area_unit[j];

            }
            AREA[area_wise_unit_price[i].id].price_by_area_unit=price_by_area_unit;
            
        }
           
      },

    error: function (request, status, error) {
        console.log(request.responseText);
    }
});


function refreshTotalPrice(){

        var option_id=$("#parcel-opton-select").val();
        var area_id=$("#area-select").val();

        var area_details=AREA[area_id];
        var parcel_option=area_details.price_by_area_unit[option_id];
        
        var base_price=parcel_option.price
        var total=base_price+ base_price*(area_details.cod_charge_percentage/100)+base_price*(area_details.return_charge_percentage/100)

        $("#total-price").val(total);



}


$(document).ready(function (event) {

 



   $("#area-select").on('change', function() {
         
        if(!this.value){
            $("#parcel-opton-select").html("<option selected>Choose Parcel Option...</option>");
            $("#total-price").val(0);
            return;

        
        
        }
        var parcel_options=AREA[this.value].price_by_area_unit
        console.log(parcel_options);

        var option_str="";

         for(id in parcel_options ){
            console.log(id);
            
            option_str=option_str+ "<option value="+ +id  +">"+parcel_options[id].quantity_price_title+"</option>";
            
        }

        $("#parcel-opton-select").html(option_str);


         refreshTotalPrice();



     });


     $("#parcel-opton-select").on('change', function() {
            refreshTotalPrice();


     });







});

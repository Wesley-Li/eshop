$(document).ready(function() {
    /*
	$('#product-images-large').magnificPopup({
        delegate: 'a',
        type: 'image',
        gallery: {
            enabled: true,
        }
    });
    */
    
    $("#wnidialog").dialog({
        autoOpen:false,
        modal:true,
    });
    
    $("#add_to_cart").click(function(){
    	//alert("shit");
    	var tmp_dict = {};
    	tmp_dict['quantity'] = $("input[name='quantity']").val()
    	var options = $("select[id^=id]");
    	for(var i=0;i<options.length;i++){
    	  tmp_dict[options[i].name] = options[i].value;
    	}
    	
    	$.ajax({
    		type:'post',
    		//async:false,
    		url: window.location.href,
    		data:tmp_dict,
    		});
    	$("#wnidialog").dialog("open");
    });
    
    $(".wniprodcont").css("color","#5a362a");
    $("label").css('color','#ffc001');
    //$('.easyzoom').easyZoom();
});
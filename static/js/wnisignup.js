$(document).ready(function() {
	//alert("shit");
	$(".input_id_username").css("display","none");
	$("#id_email").on("change",function(){
		//alert("shit");
		if($("#id_email").val()==""){$(".wemerr").remove();return false;};
		$.ajax({
		       type:'post',
		       async:false,
		       url: '/ckue/',
		       data:{'em':$("#id_email").val()},
		       success: function(html, status) {
		    	   //qunt_err=$(html).find(".errorlist");
		    	   if (html=="1"){
		  			 //$("form.cart-form").prepend(qunt_err);
		    		 if($(".wemerr").length==0){  
		    		 $(".input_id_email").append('<p class="wemerr" style="color:red;">邮件地址已被注册</p>');}
		  			 return false;
		  		 }else{$(".wemerr").remove();}}
		       });
		
		$("#id_username").val($("#id_email").val());	
	});
	$(".input_id_date_of_birth").css("display","none");
	$(".input_id_gender").css("display","none");
	$(".input_id_cell").css("display","none");
	$(".input_id_date_of_birth").before("<input type='checkbox' name='detail_info' id='id_detail_info'>填写补充信息</input><br /><br />");
	$("#id_detail_info").click(function(){$(".input_id_date_of_birth").toggle();
	$(".input_id_gender").toggle();
	$(".input_id_cell").toggle();
	});
	

});
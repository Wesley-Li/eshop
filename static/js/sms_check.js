$(document).ready(function(){
      
    $("#auth_first_check").dialog({
        autoOpen:false,
        modal:true,
        draggable:false,
    });
    
    function resendaj(){
    	if ($("#resend").attr("disabled")=="disabled"){return};
    	alert("shit");
    	resendac();
    	//return true;
    }
    
    function resendac(){
    	$("#errpane").text("");
    	timerMax=10;
    	//if ($("#resend").css("background")=="#999"){return};
    	$("#resend").css("background","#999").attr("disabled",true).click(function(event){return false;});
    	
    	//$("#countdonw").css('display','block');
    	var timer = window.setInterval(function() {
            $("#countdown").text("("+timerMax+"s)");
            if (timerMax-- <= 0) {
              window.clearInterval(timer); 
              //$("#countdonw").css('display','none');
              $("#countdown").text("");
              $("#resend").css("background","#42abff").attr("disabled",false);
              $("#resend").click(function(){resendaj();});
            }
          }, 1000);
    };
    
    $("#check_auth").click(function(){
    	$("#errpane").text("");
    	$.ajax({
    		type:'post',
    		url: '/pushsms/',
    		async: false,
    		data:{"cn":$("#auth_tel").text(),"ca":$("#vcode_input").val(),"tp":1},
    		success:function(msg){
    		if(msg == 999){
    		$("#auth_first_check").dialog("close");
    		}else{
    		$("#errpane").text("验证码错误,请重新获取!");
    		}
    		},
    		error:function(){
    		alert("网络异常!");
    		}
    		});

    });
    
   function enablesms(){	
	   alert("wnitest");
	    $("#auth_tel").text($("#id_billing_detail_phone").val());
    	$("#auth_first_check").dialog("open");
    	resendac();
    };
});
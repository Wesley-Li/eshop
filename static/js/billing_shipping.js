$(document).ready(function(){
		Date.prototype.Format = function(fmt)   
		{  
		  var o = {   
		    "M+" : this.getMonth()+1,                 
		    "d+" : this.getDate(),                     
		    "h+" : this.getHours(),   
		    "m+" : this.getMinutes(),                    
		    "s+" : this.getSeconds(),                   
		    "q+" : Math.floor((this.getMonth()+3)/3),    
		    "S"  : this.getMilliseconds()   
		  };   
		  if(/(y+)/.test(fmt))   
		    fmt=fmt.replace(RegExp.$1, (this.getFullYear()+"").substr(4 - RegExp.$1.length));   
		  for(var k in o)   
		    if(new RegExp("("+ k +")").test(fmt))   
		  fmt = fmt.replace(RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length)));   
		  return fmt;   
		}; 
   /*
	var logic = function( currentDateTime,$input ){
		var curr = new Date().getDate();
		if( currentDateTime.getDate()== curr ){
			var tmpd = new Date();
			tmpd.setHours(tmpd.getHours() + 1);
			this.setOptions({
				minTime:tmpd,
				//startDate:tmpd,
				//defaultDate:tmpd,
				//formatTime:'H:i',
				//formatDate:'Y-m-d',
				//defaultDate:new Date(), // it's my birthday
				//defaultTime:'23:00',
			});
		}else{
			this.setOptions({
				minTime:'00:00',
			//startDate:	new Date(),
			});
		}};
	$("label[for='id_prefer_time_1']").after("&nbsp;&nbsp;<input type='text' id='booktime' style='display:none;' />");
	$("#id_prefer_time_0").click(function(){$("#booktime").css("display","none");});
	var tmpt = new Date();
	tmpt.setHours(tmpt.getHours() + 2);
	$("#booktime").val('预约'+tmpt.Format("yyyy-MM-dd hh:mm"));
	$('#id_prefer_time_1').val('预约'+tmpt.Format("yyyy-MM-dd hh:mm"));
	$('#id_prefer_time_1').click(function(){
		var tmpt = new Date();
		tmpt.setHours(tmpt.getHours() + 2);
		$("#booktime").css("display","").attr("readonly","readonly");
		
		$('#booktime').datetimepicker({
			dayOfWeekStart : 1,
			lang:'ch',
			format : 'Y-m-d H:i',
			minDate : 0,
			roundTime:'ceil',
			//closeOnWithoutClick: false,
			//value:'预约2011-1-1 10:00',
			//minTime : 0,
			//startDate:tmpt,
			//setDate:new Date(),
			step:30,
			onClose: function(current_time,$input){$("#id_prefer_time_1").val("预约"+$("#booktime").val())},
			//onChangeDateTime:logic,
			onSelectDate:logic,
			onShow:logic,
			//onGenerate:logic,
			defaultTime:tmpt.getHours()+":00",
		});
	});
	*/
		
	check = 0;
	check2 = 6e6;
	function sleep(milliseconds) {
		  var start = new Date().getTime();
		  for (var i = 0; i < 1e7; i++) {
		    if ((new Date().getTime() - start) > milliseconds){
		      break;
		    }
		  }
		};	
	$(".pull-right").click(function(){
		//alert("shit");
		
		if(check!=7e7){
		$.ajax({
    		type:'post',
    		url: '/checkcell/',
    		async: false,
    		data:{"cn":$("#id_billing_detail_phone").val()},
    		success:function(msg){
    		
    			if(msg=="1"){
    				check2 = 5e5;
    				if(check!=7e7){ 
    					enablesms();
    					}
    			}    		
    		},
    		error:function(XMLHttpRequest, textStatus, errorThrown){
    		//alert("网络异常!");
    		alert(XMLHttpRequest.readyState + XMLHttpRequest.status + XMLHttpRequest.responseText);
    		}
    		});};
    		if(check!=7e7 && check2==5e5){return false;};
    	 /*
    		if($('#id_pay_type_1:checked').length==1){
    	 $.ajax({
     	       type:'get',
     	       async:false,
     	       url: '{% url "weixin:getjsparam" %}',
     	       data:{signurl:window.location.href},
     	       dataType:'text',
     	       success: function(html, status) {
     	    	//alert(html);   
     	    	eval("var allparams = "+html);
     	    	//alert(allparams);
     	    	wx.config({
        	      debug: true,
        	      appId: allparams["appId"],
        	      timestamp: allparams["timestamp"],
        	      nonceStr: allparams["nonceStr"],
        	      signature: allparams["signature"],
        	      jsApiList: [
        	        'checkJsApi',
        	        'onMenuShareTimeline',
        	        'onMenuShareAppMessage',
        	        'onMenuShareQQ',
        	        'onMenuShareWeibo',
        	        'hideMenuItems',
        	        'showMenuItems',
        	        'hideAllNonBaseMenuItem',
        	        'showAllNonBaseMenuItem',
        	        'translateVoice',
        	        'startRecord',
        	        'stopRecord',
        	        'onRecordEnd',
        	        'playVoice',
        	        'pauseVoice',
        	        'stopVoice',
        	        'uploadVoice',
        	        'downloadVoice',
        	        'chooseImage',
        	        'previewImage',
        	        'uploadImage',
        	        'downloadImage',
        	        'getNetworkType',
        	        'openLocation',
        	        'getLocation',
        	        'hideOptionMenu',
        	        'showOptionMenu',
        	        'closeWindow',
        	        'scanQRCode',
        	        'chooseWXPay',
        	        'openProductSpecificView',
        	        'addCard',
        	        'chooseCard',
        	        'openCard'
        	      ]
        	  });
     	    	wx.chooseWXPay({
                 timestamp: allparams["pay_params"]['timeStamp'], 
                 nonceStr: allparams["pay_params"]["nonceStr"], 
                 package: allparams["pay_params"]["package"], 
                 signType: allparams["pay_params"]["signType"], 
                 paySign: allparams["pay_params"]["paySign"], 
                 success: function (res) {
              	   //alert(res);
              	   
              	   if(res.errMsg == "chooseWXPay:ok" )  
      	             {  
      	                  alert("支付成功");  
      	             }
      	    	    else{
      	    	    	alert(res.err_msg);
      	    	    	return false;
      	    	    } 
                  }
             });
  	},
  	error: function(XMLHttpRequest, textStatus, errorThrown){
      		alert(errorThrown);
      		return false;
     }})};*/
    	 
	});
	
	$("#auth_first_check").dialog({
        autoOpen:false,
        modal:true,
        draggable:false,
        open: function(event, ui) { $(".ui-dialog-titlebar").hide();},
    });
    
    function resendaj(){
    	if ($("#resend").attr("disabled")=="disabled"){return};
    	//alert("shit");
    	$.ajax({
    		type:'post',
    		url: '/pushsms/',
    		async: false,
    		data:{"cn":$("#auth_tel").text(),"tp":0},
    		success:function(msg){
    		if(msg == "1"){
    		 return 1;
    		}else{
    		$("#errpane").text("验证码错误,请重新获取!");
    		};
    		},
    		error:function(){
    		alert("网络异常!请重新获取验证码!");
    		}
    		});
    	resendac();

    };
    
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
    
    function submitcheck(){
    	$("#errpane").text("");
    	$.ajax({
    		type:'post',
    		url: '/pushsms/',
    		async: false,
    		data:{"cn":$("#auth_tel").text(),"ca":$("#vcode_input").val(),"tp":1},
    		success:function(msg){
    		if(msg == 999){
    		check = 7e7;
    		$("#auth_first_check").dialog("close");
    		$(".pull-right").click();
    		
    		}else{
    		$("#errpane").text("验证码错误,请重新获取!");
    		//window.location.href="/shop/checkout";
    		};
    		},
    		error:function(XMLHttpRequest, textStatus, errorThrown){
    		alert("网络异常!");
    		}
    		});
    };
    
    $("#check_auth").click(submitcheck);
    
   function enablesms(){	
	    $("#auth_tel").text($("#id_billing_detail_phone").val());
    	$("#auth_first_check").dialog("open");
    	resendac();
    };
    $('#id_delivery_type_1').css("display","none");
    if($('#id_delivery_type_0_1:checked').length==1){$('#id_delivery_type_1').css("display","");};
    $('#id_delivery_type_0_1').on("click",function(){$('#id_delivery_type_1').css("display","");});
    $('#id_delivery_type_0_0').on("click",function(){$('#id_delivery_type_1').css("display","none");});
    /*
    $("#wnicheckoutnext").click(function(){
    	if($('#id_pay_type_1:checked').length==1){
    		$.ajax({
       	       type:'get',
       	       async:false,
       	       url: '{% url "weixin:getjsparam" %}',
       	       success: function(html, status) {
       	    	   
       	    	eval("var allparams = "+html);
       	    	
       	    	wx.config({
          	      debug: false,
          	      appId: allparams["appId"],
          	      timestamp: allparams["timestamp"],
          	      nonceStr: allparams["nonceStr"],
          	      signature: allparams["signature"],
          	      jsApiList: [
          	        'checkJsApi',
          	        'onMenuShareTimeline',
          	        'onMenuShareAppMessage',
          	        'onMenuShareQQ',
          	        'onMenuShareWeibo',
          	        'hideMenuItems',
          	        'showMenuItems',
          	        'hideAllNonBaseMenuItem',
          	        'showAllNonBaseMenuItem',
          	        'translateVoice',
          	        'startRecord',
          	        'stopRecord',
          	        'onRecordEnd',
          	        'playVoice',
          	        'pauseVoice',
          	        'stopVoice',
          	        'uploadVoice',
          	        'downloadVoice',
          	        'chooseImage',
          	        'previewImage',
          	        'uploadImage',
          	        'downloadImage',
          	        'getNetworkType',
          	        'openLocation',
          	        'getLocation',
          	        'hideOptionMenu',
          	        'showOptionMenu',
          	        'closeWindow',
          	        'scanQRCode',
          	        'chooseWXPay',
          	        'openProductSpecificView',
          	        'addCard',
          	        'chooseCard',
          	        'openCard'
          	      ]
          	  });
       	       
       	    	  //alert(html);
       	    	 // alert(status);
       	    	   WeixinJSBridge.invoke(
       	                   'getBrandWCPayRequest',
       	                   allparams["pay_params"],
       	                   function(res){
       	                       //WeixinJSBridge.log(res.err_msg);
       	                       //alert(res.err_code+res.err_desc+res.err_msg);
       	                	if(res.err_msg != "get_brand_wcpay_request:ok" ) {
       	                		alert("支付失败,请检查微信支付帐号");
       	                		return false;
       	                	   }
       	                	}
       	               );
       	       //},//alert(html);},
       	      //error: function(XMLHttpRequest, textStatus, errorThrown){
       	    		//alert("缃戠粶寮傚父!");
       	    //		alert(errorThrown);
       	   // 		}
       	   //    });
    	},
    	error: function(XMLHttpRequest, textStatus, errorThrown){
	    		alert(errorThrown);
	    		return false;
    }}); */
});
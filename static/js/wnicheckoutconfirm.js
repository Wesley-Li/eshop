$(document).ready(function(){
    var wx_success = false;
	//weixinpay start
	$("#wnicheckoutnext").click(function(nextevet){
		//alert("confirm button clicked!");
		//alert($("#id_pay_type").val());
		if($("#id_pay_type").val()=="微信支付"){
			//alert('preajax');
			 if(wx_success){return true};
	    	 $.ajax({
	    		 type:'get',
	     	       async:false,
	     	       //url: '{% url "weixin:getjsparam" %}',
	     	       url: '/weixin/getjspayparam/',
	     	       data:{signurl:window.location.href},
	     	       dataType:'text',
	     	       success: function(html, status) {
	     	    	//alert(html);   
	     	    	eval("var allparams = "+html);
	     	    	//alert(allparams);
	     	    	wx.config({
	        	      debug: false,
	        	      appId: allparams["appId"],
	        	      timestamp: allparams["timestamp"],
	        	      nonceStr: allparams["nonceStr"],
	        	      signature: allparams["signature"],
	        	      jsApiList: [
	        	        
                                //'checkJsApi',
	        	        //'onMenuShareTimeline',
	        	        //'onMenuShareAppMessage',
	        	        //'onMenuShareQQ',
	        	        //'onMenuShareWeibo',
	        	        //'hideMenuItems',
	        	        //'showMenuItems',
	        	        //'hideAllNonBaseMenuItem',
	        	        //'showAllNonBaseMenuItem',
	        	        //'translateVoice',
	        	        //'startRecord',
	        	        //'stopRecord',
	        	        //'onRecordEnd',
	        	        //'playVoice',
	        	        //'pauseVoice',
	        	        //'stopVoice',
	        	        //'uploadVoice',
	        	        //'downloadVoice',
	        	        //'chooseImage',
	        	        //'previewImage',
	        	        //'uploadImage',
	        	        //'downloadImage',
	        	        //'getNetworkType',
	        	        //'openLocation',
	        	        //'getLocation',
	        	        //'hideOptionMenu',
	        	        //'showOptionMenu',
	        	        //'closeWindow',
	        	        //B
	        	        //'scanQRCode',
	        	        'chooseWXPay',
	        	        //'openProductSpecificView',
	        	        //'addCard',
	        	        //'chooseCard',
	        	        //'openCard'
	        	      ]
	        	  });
                        //alert("after config");
                        //wx.error(function(res){alert(res);});
	     	    	$("form.checkout-form").submit(function(){return false;});
                        //alert("before pay");
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
	      	                  //alert("支付成功");
	      	                //$("form.checkout-form").submit();
	              		//$("#wnicheckoutnext").click(function(){return true});
	              		$("form.checkout-form").unbind("submit");   
	              		$("form.checkout-form").submit(function(){return true;});
	              		wx_success = true;
	              		$("#wnicheckoutnext").click();
	      	             }
	      	    	    else{
	      	    	    	//alert("支付失败!"); 
	      	    	    	alert(res.errMsg);
	      	    	    	nextevet.preventDefault();
	      	    	    	return false;
	      	    	    } 
	                  }
	             });
	  	},
	  	error: function(XMLHttpRequest, textStatus, errorThrown){
	  		alert('ajax error caught!');
	      		alert(errorThrown);
	      		//var payerr=true;
	      		nextevet.preventDefault();
	      		return false;
	     }})}
	   //alert(payerr);
	   //if(payerr){return false;};  
	});
});

$(document).ready(function(){
	function udt_ct(ctda){
		$.ajax({
		       type:'post',
		       async:false,
		       url: '/shop/cart/',
		       data:ctda,
		       success: function(html, status) {wni_dict=tmp(html)}
		       //wni:need to filter if errorlist returned
		       });
	};
	function tmp(wnihtml){
		if(wnihtml==null){
		String.prototype.format = function () {
		        var args = [].slice.call(arguments);
		        return this.replace(/(\{\d+\})/g, function (a){
		            return args[+(a.substr(1,a.length-2))||0];
		        });
		};
		var init_dict = {};
		init_dict['items-TOTAL_FORMS']=$("#id_items-TOTAL_FORMS").val();
		init_dict['items-INITIAL_FORMS']=$("#id_items-INITIAL_FORMS").val();
		init_dict['items-MAX_NUM_FORMS']=$("#id_items-MAX_NUM_FORMS").val();
		init_dict['update_cart'] = "update";
		
		for(x=0;x<init_dict['items-TOTAL_FORMS'];x++)
		{
		  var id = 'items-{0}-id'.format(x);
		  var quantity = 'items-{0}-quantity'.format(x);
		  init_dict[id] = $("input[name={0}]".format(id)).val();
		  init_dict[quantity] = $("input[name={0}]".format(quantity)).val();
		};
		return init_dict;}
		else{
			var init_dict = {};
			init_dict['items-TOTAL_FORMS']=$("#id_items-TOTAL_FORMS",wnihtml).val();
			init_dict['items-INITIAL_FORMS']=$("#id_items-INITIAL_FORMS",wnihtml).val();
			init_dict['items-MAX_NUM_FORMS']=$("#id_items-MAX_NUM_FORMS",wnihtml).val();
			init_dict['update_cart'] = "update";
			
			for(x=0;x<init_dict['items-TOTAL_FORMS'];x++)
			{
			  var id = 'items-{0}-id'.format(x);
			  var quantity = 'items-{0}-quantity'.format(x);
			  init_dict[id] = $("input[name={0}]".format(id),wnihtml).val();
			  init_dict[quantity] = $("input[name={0}]".format(quantity),wnihtml).val();
			};
			return init_dict;
		}
		}
	wni_dict = tmp();
	$("input[name='update_cart']").css('display','none');
	
	$(":checkbox[name$='DELETE']").click(function(){
		if (confirm("确定要删除该商品吗？")){
		
			$(this).parents("tr").css("display","none");
    var tmp_price = parseFloat($(this).parent().prev().text());
    var old_total = parseFloat($(".total").children("span").text());
    var final_total = old_total - tmp_price;
    $(".total").children("span").text(String(final_total));
    
    //wni_dict[$(this).attr('name')] = "on";
    var wnitmp = $(this).parents("tr").prevAll('tr:not([style])').length
    wni_dict['items-{0}-DELETE'.format(wnitmp)] = "on";
    udt_ct(wni_dict);
			//$("input[name='update_cart']").click();
		}
		else{
			$(this).prop("checked",false);
		}
 });
	
	$("input[name$=quantity]").on("change",function(){
		
		//alert($(this).attr('name'));
		//var unit_price = parseFloat($(this).parent().prev().text());
		//var item_total = parseFloat($(this).parent().next().text());
	    //var old_total = parseFloat($(".total").children("span").text());
	    var old_quantity = parseInt(wni_dict[$(this).attr('name')]);
	    var current_quantity = parseInt($(this).val());
	    
	    //var item_total_changed = (current_quantity - old_quantity) * unit_price;
	    //var final_item_total = item_total + item_total_changed;
	    //var final_total = old_total + item_total_changed;
	    
	    //$(this).parent().next().text(final_item_total);
	    //$(".total").children("span").text(String(final_total));
	    //wni_dict[$(this).attr('name')]=current_quantity;
	    //udt_ct(wni_dict);
	    
	    qunt_err = null;
	    var wni_tmp_dict = wni_dict;
	    wni_tmp_dict[$(this).attr('name')]=current_quantity;
	    $.ajax({
		       type:'post',
		       async:false,
		       url: '/shop/cart/',
		       data:wni_tmp_dict,
		       success: function(html, status) {qunt_err=$(html).find(".errorlist");}
		       });
	    if (qunt_err.length>0){
			 $("form.cart-form").prepend(qunt_err);
			 wni_tmp_dict[$(this).attr('name')]=old_quantity;
			 $(this).val(old_quantity);
		 }else{
			 var unit_price = parseFloat($(this).parent().prev().text());
				var item_total = parseFloat($(this).parent().next().text());
			    var old_total = parseFloat($(".total").children("span").text());
			    //var old_quantity = parseInt(wni_dict[$(this).attr('name')]);
			    var item_total_changed = (current_quantity - old_quantity) * unit_price;
			    var final_item_total = item_total + item_total_changed;
			    var final_total = old_total + item_total_changed;
			    wni_dict[$(this).attr('name')]=current_quantity;
			    //alert("old_total"+old_total);
			    //alert("old qunt"+old_quantity);
			    //alert("curr qunt"+current_quantity);
			    //alert("item total changed"+item_total_changed);
			 $(this).parent().next().text(final_item_total);
			 $(".total").children("span").text(String(final_total)); 
		 }
		//$("input[name='update_cart']").click();
 });
  
  check_err = null;
  function tmp_func(){window.location.href='/shop/checkout/'};
  $("a[href='/shop/checkout/']").click(function(e){
	  //e.preventDefault();
	 //alert('shit');
	 //$('input[name="update_cart"]').queue($(this).click());
	 //$('input[name="update_cart"]').queue(function(){$(this).click();$(this).dequeue();alert('fuck');});
	 //wni_dict=tmp();
	 $.ajax({
       type:'post',
       async:false,
       url: '/shop/cart/',
       data:wni_dict,//{'items-0-id':142,'items-1-id':148,'items-0-quantity':3,'update_cart':'update','items-TOTAL_FORMS':2,'items-INITIAL_FORMS':2,'items-MAX_NUM_FORMS':1000,'items-1-quantity':1,'items-1-DELETE':'on'},//{'items-0-quantity':4,'update_cart':'update','items-TOTAL_FORMS':1,'items-INITIAL_FORMS':1,'items-MAX_NUM_FORMS':1000,'items-0-id':142},
       success: function(html, status){check_err=$(html).find(".errorlist");} //{alert($(html).find(".errorlist").html());}
       });
	 //tmp_func();
	 //window.location.href = '/shop/checkout/';
	 if (check_err.length>0){
		 $("form.cart-form").prepend(check_err);
		 return false;
	 }
  });
  
  
  $("#mydiscount").click(function(e){
	   $.ajax({
       type:'get',
       async:false,
       url: '/ajmydiscount/',
       success: function(html, status) {$(html).dialog({
           //autoOpen: false,
           modal: true,
           width: 550,
           draggable: false,
           //height:650,
           title: '我的优惠券'
           });},//alert(html);},
       });
  });
  
  $(".useclick").live('click',function(){
		$('#id_discount_code').val($(this).parent().siblings().slice(1,2).text());
		$('#cart_discount').dialog('destroy');
	});
  $("label[for='id_discount_code']").text("输入优惠券号码");
  //$.ajax({
  //    type:'get',
  //    async:false,
  //    url: '/onekey/',
  //    success: function(html, status){$("#oneclick").attr('href',$("#oneclick").attr('href')+'?'+html);} //{alert($(html).find(".errorlist").html());}
  //    });
  
});
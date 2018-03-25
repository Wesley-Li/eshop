$(document).ready(function(){
     $("#ad_sidebar a").mouseover(function(){$(this).next().css("display","inline");});
     $("#ad_sidebar a").mouseout(function(){$(this).next().css("display","none");});
     
     $(".editable-original").css("color","#5a362a");

});

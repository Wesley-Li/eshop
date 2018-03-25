$(document).ready(function(){
	$("#searchline").css("display",'none');
	$(".navbar-nav > li>a").click(function(){
		$(".navbar-nav > li>a").css("border-bottom-width","0");
		$(this).css("border-bottom","2px solid black");
	});
})
jQuery(document).ready(function(){
	jQuery("#carousel-example-generic").touchwipe({
          wipeLeft: function() { jQuery("#carousel-example-generic").carousel('next'); },
          wipeRight: function() { jQuery("#carousel-example-generic").carousel('prev'); },
          min_move_x: 20,
          preventDefaultEvents: true,
	});
});
$(document).ready(function() {
  // Increase header tags by one
  for (var i=5; i>0; i--) {
    // Iterate over each element and replace tag while maintaining attributes
    $('.notebook h'+i).each(function() {
      $(this).replaceWith(function() {
        return $(this).replaceTag('h'+(i+1), true);
      });
    });
  }
});

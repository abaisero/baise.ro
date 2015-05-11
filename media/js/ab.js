$(function() {
  // obfuscates email
  $("a.email").each(function(i) {
    $(this).text($(this).attr("href").replace("[AT]", "@").replace(/\[DOT\]/g, "."));
    $(this).attr("href", "mailto:" + $(this).text());
  });

  // move contents of paragraphs to parent, and delete paragraph.
  // because kramdown inserts paragraphs everywhere.
  $("p.remove").each(function(i) {
    $(this).contents().appendTo($(this).parent());
    $(this).remove();
  });

  // insert stuff
  $(".include").each(function (i) {
    $(this).load($(this).attr("url"));
  });

  // mountain goes to muhammad
  $("div.mountain").each(function (i) {
    var muhammad_id = $(this).attr("muhammad");
    var muhammad = $("span.muhammad#" + muhammad_id);

    var left = parseInt(muhammad.offset().left, 10);
    var top = parseInt(muhammad.offset().top, 10);
    // var width = parseInt($(this).width(), 10);
    // var width = $(this).css("width");
    // var width = $(this).outerWidth();
    // var width = $(this).width();
    // var width = $(this).offsetWidth();
    // var width = parseInt($(this).offsetWidth(), 10);
    // $(this).text(width + '; ' + left);
    $(this).css({
      'position': 'absolute',
      // 'left': left+'px',
      'left': left-55,
      'top': top,
      // 'background': 'blue'
    });
  });
});

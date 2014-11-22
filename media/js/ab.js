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
});

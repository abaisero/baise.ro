$(function() {

  // obfuscates email
  $("span.email").each(function(i) {
    var email = $(this).text().replace(/\[CHIOCCIOLA\]/g, "@").replace(/\[PUNTO\]/g, ".").replace(/\[TRATTINO\]/g, "-")
    $(this).text(email);
    // $(this).text($(this).attr("href").replace("[CHIOCCIOLA]", "@").replace(/\[PUNTO\]/g, ".").replace(/\[TRATTINO\]/g, "-"));
    // $(this).attr("href", "mailto:" + $(this).text());
  });

});

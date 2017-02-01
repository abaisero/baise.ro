$(function() {

  // obfuscates email
  $("span.email").each(function(i) {
    var email = $(this).text().replace(/\[CHIOCCIOLA\]/g, "@").replace(/\[PUNTO\]/g, ".").replace(/\[TRATTINO\]/g, "-")
    $(this).text(email);
    // $(this).text($(this).attr("href").replace("[CHIOCCIOLA]", "@").replace(/\[PUNTO\]/g, ".").replace(/\[TRATTINO\]/g, "-"));
    // $(this).attr("href", "mailto:" + $(this).text());
  });

  // // move contents of paragraphs to parent, and delete paragraph.
  // // because kramdown inserts paragraphs everywhere.
  // $("p.remove").each(function(i) {
  //   $(this).contents().appendTo($(this).parent());
  //   $(this).remove();
  // });

  // // insert stuff
  // $(".include").each(function (i) {
  //   $(this).load($(this).attr("url"));
  // });

  // // mountain goes to muhammad
  // $("div.mountain").each(function (i) {
  //   var muhammad_id = $(this).attr("mhd");
  //   var muhammad = $("span.muhammad#" + muhammad_id);

  //   var left = parseInt(muhammad.offset().left, 10);
  //   var top = parseInt(muhammad.offset().top, 10);
  //   // var width = parseInt($(this).width(), 10);
  //   // var width = $(this).css("width");
  //   // var width = $(this).outerWidth();
  //   // var width = $(this).width();
  //   // var width = $(this).offsetWidth();
  //   // var width = parseInt($(this).offsetWidth(), 10);
  //   // $(this).text(width + '; ' + left);
  //   $(this).css({
  //     // 'position': 'absolute',
  //     // 'left': left+'px',
  //     // 'left': left-60,
  //     // 'top': top,
  //     // 'background': 'blue'
  //   });
  // });

  // Removes style from unordered list
  $('li.nostyle').parent('ul').css({
    'list-style-type': 'none',
    'padding-left': '0pt',
  });

  // Adds appropriate Font Awesome class to iconized unordered list
  $('i.fa-li').parent('li').parent('ul').addClass('fa-ul');
});

// Wow this really sucks
function resizeIframe(obj) {
  obj.style.height = (obj.contentWindow.document.body.scrollHeight + 150) + 'px';
}


var tables = document.querySelectorAll('#content .before_table + table');
tables.forEach(function(table) {
  table.classList.add('table', 'table-striped', 'table-hover');
});

var lists = document.querySelectorAll('#content .before_lu + ul');
lists.forEach(function(list) {
  list.classList.add('fa-ul');
});


killParent('span.begin_article');
killParent('span.end_article');
var begin_articles = document.querySelectorAll('span.begin_article');
begin_articles.forEach(function(begin) {
  var article = document.createElement('article'),
      between = nextUntil(begin, 'span.end_article'),
      end = between[between.length-1].nextElementSibling;
  begin.classList.remove("begin_article");
  copyAttributes(article, begin);
  begin.insertAdjacentElement("afterend", article);
  between.forEach(function(e) { article.appendChild(e); });
  begin.remove();
  end.remove();
});

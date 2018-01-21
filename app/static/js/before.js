var tables = document.querySelectorAll('#content .before_table + table');
tables.forEach(function(table) {
  table.classList.add('table', 'table-striped', 'table-hover');
});

var lists = document.querySelectorAll('#content .before_lu + ul');
lists.forEach(function(list) {
  list.classList.add('fa-ul');
});


function processBeginTag(tagName, kp=true) {
  if (kp) {
    killParent('span.begin_'+tagName);
    killParent('span.end_'+tagName);
  }
  var begin_tags = document.querySelectorAll('span.begin_'+tagName);
  begin_tags.forEach(function(begin) {
    var tag = document.createElement(tagName),
        between = nextUntil(begin, 'span.end_'+tagName),
        end = between[between.length-1].nextElementSibling;
    begin.classList.remove('begin_'+tagName);
    copyAttributes(tag, begin);
    begin.insertAdjacentElement('afterend', tag);
    between.forEach(function(e) { tag.appendChild(e); });
    begin.remove();
    end.remove();
  });
}

processBeginTag('article', kp=true);
processBeginTag('div', kp=true);

var tables = document.querySelectorAll('#content .before_table + table');
tables.forEach(function(table) {
  table.classList.add('table', 'table-striped', 'table-hover');
});

var lists = document.querySelectorAll('#content .before_lu + ul');
lists.forEach(function(list) {
  list.classList.add('fa-ul');
});

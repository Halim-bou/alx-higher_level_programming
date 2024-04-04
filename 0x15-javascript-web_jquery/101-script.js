$(function () {
  const text = '<li>Item</li>';
  $('div#add_item').click(function () {
    $(text).appendTo('ul.my_list');
  });
  $('div#remove_item').click(function () {
    $('ul.my_list li:last-child').remove();
  });
  $('div#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});

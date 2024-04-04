#!/usr/bin/node
$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (orders) {
      $.each(orders.results, function (i, order) {
        $('ul#list_movies').append('<li>' + order.title + '</li>');
      });
    }
  });
});

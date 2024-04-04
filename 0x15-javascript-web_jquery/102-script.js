$(function () {
  $('input#btn_translate').click(function () {
    $.post('https://hellosalut.stefanbohacek.dev/', { lang: $('input#language_code').val() }, function (data) {
      $('div#hello').text(data.hello);
    });
  });
});

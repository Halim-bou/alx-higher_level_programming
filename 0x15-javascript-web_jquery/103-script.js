$(function () {
  function toTranslate () {
    $.post('https://hellosalut.stefanbohacek.dev/', { lang: $('input#language_code').val() }, function (data) {
      $('div#hello').text(data.hello);
    });
  }
  $('input#btn_translate').click(toTranslate);
  $('input#language_code').keypress(function (enter) {
    if (enter.which === 13) {
      toTranslate();
    }
  });
});

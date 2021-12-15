$(document).ready(function() {
  $('a.det-loc').each(function () {
    var href = $(this).attr("href");
    href = href.replace("localizaciones", "localizacionesAjax");
    $(this).qtip({
       content: {
          url: href,
          method: 'get'
       }
    });
  });
});
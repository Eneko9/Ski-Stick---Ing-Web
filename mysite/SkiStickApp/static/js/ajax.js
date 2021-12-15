$(document).ready(function() {

  $('a').each(function () {
    var href = $(this).attr("href");
    href = href.replace("localizaciones", "localizacionesAjax");
    alert(href);
    $(this).qtip({
       content: {
          url: href,
          method: 'get'
       }
    });
  });
});
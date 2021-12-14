$(document).ready(function() {

  $('a.link-localizaciones').each(function () {
    var href = $(this).attr("href");
    href = href.replace("post", "postAjax");
    $(this).qtip({
       content: {
          url: href,
          method: 'get'
       }
    });
  });
});
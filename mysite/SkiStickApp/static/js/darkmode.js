var modo = new Boolean(true);

function cambiar_modo() {
  if (modo) {
    let header = document.getElementById("header");
    header.style.backgroundColor = "black";

    document.body.style.backgroundColor = "#1D1D1D";

    let sitec = document.getElementById("site_content");
    sitec.style.backgroundColor = "#777";
    sitec.style.color = "white";

    let menu = document.getElementById("menubar");
    menu.style.backgroundColor = "midnightblue";

    let titprincipal = document.getElementById("logo_colour");
    titprincipal.style.color = "midnightblue";

    let titulos = document.getElementsByTagName('h2');
    for (var i = 1; i < titulos.length; i++) {
      titulos[i].style.color = "midnightblue";
    }

    let footer = document.getElementById("footer");
    footer.style.backgroundColor = "midnightblue";

    let cuadro = document.getElementById("modo");
    cuadro.style.border = "1px solid white";

    $("#modoN").attr("src", "/static/sol.png");

    modo = false;
  }else{
    location.reload();
    modo = true;
  }
}


$(document).ready(function () {
  var boton = document.getElementById('bModo');
  boton.onclick = cambiar_modo;
  
});
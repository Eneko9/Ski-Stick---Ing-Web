function cambiar_modo(){
  //TODO cambiar los estilos por modo oscuro
  let header = document.getElementById("header");
  header.style.backgroundColor = "black";


  //document.getElementById("header").style.backgroundColor = "black";
  
}
$(document).ready(function() {
    var boton = document.getElementById('bModo');
    boton.onclick = cambiar_modo;
  });
function cambiar_modo(){
  //TODO cambiar los estilos por modo oscuro
  alert('hola');
}
$(document).ready(function() {
    var boton = document.getElementById('bModo');
    boton.onclick = cambiar_modo;
  });
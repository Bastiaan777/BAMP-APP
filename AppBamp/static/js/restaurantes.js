function enviarFormulario(idRestaurante){
    document.getElementById("input-restaurante").value = idRestaurante;
    document.getElementById("formulario-oculto").submit();
}
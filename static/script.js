document.addEventListener("DOMContentLoaded", function() {
    var errorMessage = document.getElementById('error_message').textContent.trim();

    if (errorMessage && errorMessage !== 'none') {
        alert(errorMessage); // Muestra un alert con el mensaje de error si existe y no es 'none'
    }
});




function copiarContrasena() {
    var contrasenaGenerada = document.querySelector('h2').textContent.split(': ')[1]; // Obtiene solo la contraseña
    var campoTemporal = document.createElement('textarea');
    campoTemporal.value = contrasenaGenerada;

    // Agrega el campo temporal al cuerpo del documento
    document.body.appendChild(campoTemporal);

    // Selecciona el texto contenido en el campo temporal
    campoTemporal.select();
    document.execCommand('copy');

    // Elimina el campo temporal
    document.body.removeChild(campoTemporal);

    // Genera el mensaje
    alert('¡Contraseña copiada al portapapeles!');
}







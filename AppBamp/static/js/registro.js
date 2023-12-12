window.onload = function() {
    var cerrarAlerta = document.getElementById("closeModalAlerta");
    cerrarAlerta.onclick = function() {
        var modal = document.getElementById("modalAlerta");
        modal.style.display = "none";
    }
    var cerrarErrores = document.getElementById("closeModalErrores");
    if (cerrarErrores) {
        cerrarErrores.onclick = function() {
            var modal = document.getElementById("modalErrores");
            modal.style.display = "none";
        }    
    }

    // Añadir evento de entrada para el campo de usuario
    var inputUsuario = document.getElementById("usuario");
    inputUsuario.addEventListener('change', function() {
        verificarUsuario(this.value)
    });
}


function verificarUsuario(username) {
    console.log("El username es: " + username);
    if (username.length === 0) {
        
        return;
    }

    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://127.0.0.1:8000/accounts/verificar-usuario?username=' + username, true);
    xhr.onload = function() {
        if (this.status == 200) {
            var jsonResponse = JSON.parse(this.responseText);
            console.log("jsonResponse is: " + jsonResponse);
            if (jsonResponse.usuarioExiste) {
                mostrarAlerta("Ya existe este usuario");
                
            }
        }
    };
    xhr.send();
}
function mostrarAlerta(mensaje) {
    var textoAlerta = document.getElementById("textoAlerta");
    textoAlerta.innerHTML = mensaje;
    var modal = document.getElementById("modalAlerta");
    modal.style.display = "block";
}

function validarFormulario() {
    var usuario = document.getElementById("usuario").value;
    var email = document.getElementById("email").value;
    var firstName = document.getElementById("first_name").value;
    var lastName = document.getElementById("last_name").value;
    var password1 = document.getElementById("password1").value;
    var password2 = document.getElementById("password2").value;
    var fechaNacimiento = document.getElementById("fecha").value;
    var direccion = document.getElementById("direccion").value;

    if (usuario === '' || email === '' || firstName === '' || lastName === '' || password1 === '' || password2 === '' || fechaNacimiento === '' || direccion === '') {
        mostrarAlerta("Por favor, rellene todos los campos.");
        return false;
    }

    if (!/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(email)) {
        mostrarAlerta("Ingrese un correo electrónico válido.");
        return false;
    }    

    if (password1.length < 8) {
        mostrarAlerta("La contraseña debe tener al menos 8 caracteres.");
        return false;
    } 

    if (!/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/.test(password1)) {
        mostrarAlerta("La contraseña debe incluir números, mayúsculas y minúsculas.");
        return false;
    }

    if (password1 !== password2) {
        mostrarAlerta("Las contraseñas no coinciden.");
        return false;
    }

    return true;
}

function showPassword(passwordFieldId) {
    var passwordField = document.getElementById(passwordFieldId);
    passwordField.type = 'text';
}

function hidePassword(passwordFieldId) {
    var passwordField = document.getElementById(passwordFieldId);
    passwordField.type = 'password';
}

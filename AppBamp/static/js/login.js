function togglePasswordVisibility(fieldId) {
    var passwordField = document.getElementById(fieldId);
    var type = passwordField.type === 'password' ? 'text' : 'password';
    passwordField.type = type;
  }
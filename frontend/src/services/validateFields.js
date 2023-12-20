function isValidNameFormat(name) {
    const nameRegex = /^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$/;
    return nameRegex.test(name);
  }

function validateName(name) {
  let message = "";
  let nameValue;

  if (name) {
    nameValue = name.trim();
  } else {
    return message;
  }

  if (!nameValue) {
    message = 'Nome é requerido!';
  } else if (!isValidNameFormat(nameValue)) {
    message = 'Nome inválido.';
  }
  return message;
}


function isValidEmailFormat(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

function validateEmail(email) {
  let message = "";
  let emailValue;

  if (email) {
    emailValue = email.trim();
  } else {
    return message;
  }
  
  if (!emailValue) {
    message = "Email é requerido!";
  } else if (!isValidEmailFormat(emailValue)) {
    message = "Email inválido!";
  }
  return message;
}

function validatePosition(name) {
  let message = "";
  let nameValue;

  if (name) {
    nameValue = name.trim();
  } else {
    return message;
  }

  if (!nameValue) {
    message = 'Cargo inválido';
  } else if (!isValidNameFormat(nameValue)) {
    message = 'Cargo inválido.';
  }
  return message;
}

function validatePassword(password) {
  let message = ""
  if (password && password.length < 6) message = "Senha curta!"
  return message
}

function validateCardInputs(text) {
  let message = "";
  let textValue;

  if (text) {
    textValue = text.trim();
  } else {
    return message;
  }

  if (!textValue) {
    message = 'O valor digitado é inválido.';
  }
  return message;
}

export {
  validateName,
  validateEmail,
  validatePosition,
  validatePassword,
  validateCardInputs,
}
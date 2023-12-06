const TOKEN = "@TOKEN"
const EMAIL = "@EMAIL"
const USERNAME = "@USERNAME"

function get_token() {
    return localStorage.getItem(TOKEN)
}

function set_token(tk) {
    localStorage.setItem(TOKEN, tk)
}

function get_email() {
    return localStorage.getItem(EMAIL)
}

function set_email(em) {
    localStorage.setItem(EMAIL, em)
}

function get_username() {
    return localStorage.getItem(USERNAME)
}

function set_username(un) {
    localStorage.setItem(USERNAME, un)
}

function isAuthenticated() {
    if (get_token()) return true;
    return false;
}

function logout() {
    localStorage.removeItem(EMAIL)
    localStorage.removeItem(TOKEN)
    localStorage.removeItem(USERNAME)
}

export {
    get_token, 
    set_token, 
    get_email, 
    set_email,
    get_username,
    set_username,
    isAuthenticated,
    logout,
}
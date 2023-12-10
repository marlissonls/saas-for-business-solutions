const TOKEN = "@TOKEN";
const ID = "@ID";
const USERNAME = "@USERNAME";
const EMAIL = "@EMAIL";
const ROLE = "@ROLE"

function get_token() {
    return localStorage.getItem(TOKEN)
}

function set_token(tk) {
    localStorage.setItem(TOKEN, tk)
}

function get_id() {
    return localStorage.getItem(ID)
}

function set_id(id) {
    localStorage.setItem(ID, id)
}

function get_username() {
    return localStorage.getItem(USERNAME)
}

function set_username(un) {
    localStorage.setItem(USERNAME, un)
}

function get_email() {
    return localStorage.getItem(EMAIL)
}

function set_email(em) {
    localStorage.setItem(EMAIL, em)
}

function get_role() {
    return localStorage.getItem(ROLE)
}

function set_role(rl) {
    localStorage.setItem(ROLE, rl)
}

function isAuthenticated() {
    if (get_token()) return true;
    return false;
}

function isAdmin() {
    if (get_role() === 'admin') return true;
    return false;
}

function logout() {
    localStorage.removeItem(EMAIL)
    localStorage.removeItem(TOKEN)
    localStorage.removeItem(USERNAME)
    localStorage.removeItem(ID)
    localStorage.removeItem(ROLE)
}

export {
    get_token, 
    set_token, 
    get_email, 
    set_email,
    get_username,
    set_username,
    get_id,
    set_id,
    get_role,
    set_role,
    isAuthenticated,
    isAdmin,
    logout,
}
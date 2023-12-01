const TOKEN = "@TOKEN"
const USERNAME = "@USERNAME"

function getToken() {
    return localStorage.getItem(TOKEN)
}

function setToken(tk) {
    localStorage.setItem(TOKEN, tk)
}

function getUsername() {
    return localStorage.getItem(USERNAME)
}

function setUsername(un) {
    localStorage.setItem(USERNAME, un)
}

function isAuthenticated() {
    if (getToken()) return true;
    return false;
}

function logout() {
    localStorage.removeItem(USERNAME)
    localStorage.removeItem(TOKEN)
}

export {
    getToken, 
    setToken, 
    getUsername, 
    setUsername, 
    isAuthenticated,
    logout,
}
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

export {getToken, setToken, getUsername, setUsername}
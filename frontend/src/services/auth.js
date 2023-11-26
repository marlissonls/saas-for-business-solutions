const TOKEN = "@TOKEN"

function getToken() {
    return localStorage.getItem(TOKEN)
}

function setToken(tk) {
    localStorage.setItem(TOKEN, tk)
}

export {getToken, setToken}
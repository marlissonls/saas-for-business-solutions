const TOKEN = "@TOKEN";
const ID = "@ID";
const USERNAME = "@USERNAME";
const EMAIL = "@EMAIL";
const ROLE = "@ROLE";
const PHOTO = "@PHOTO";
const POSITION = "@POSITION";
const COMPANY = "@COMPANY";
const COMPANYID = "@COMPANYID";

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

function get_photo_url() {
    return localStorage.getItem(PHOTO)
}
function set_photo_url(pf) {
    localStorage.setItem(PHOTO, pf)
}

function get_position() {
    return localStorage.getItem(POSITION)
}
function set_position(pt) {
    localStorage.setItem(POSITION, pt)
}

function get_company() {
    return localStorage.getItem(COMPANY)
}
function set_company(cp) {
    localStorage.setItem(COMPANY, cp)
}

function get_company_id() {
    return localStorage.getItem(COMPANYID)
}
function set_company_id(cpid) {
    localStorage.setItem(COMPANYID, cpid)
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
    localStorage.removeItem(PHOTO)
    localStorage.removeItem(POSITION)
    localStorage.removeItem(COMPANY)
    localStorage.removeItem(COMPANYID)
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
    get_photo_url,
    set_photo_url,
    get_position,
    set_position,
    get_company,
    set_company,
    get_company_id,
    set_company_id,
    isAuthenticated,
    isAdmin,
    logout,
}
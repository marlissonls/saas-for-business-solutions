import React, { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useSnackbar } from 'notistack';

import { validateEmail, validatePassword } from "../../services/validateFields";
import { set_token, set_id, set_email, set_username, set_role } from "../../services/auth";
import api from "../../services/api";

function Login(props) {

  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")

  const { enqueueSnackbar } = useSnackbar()

  const navigate = useNavigate()

  function getErrors() {
    const errors = []
    errors[0] = validateEmail()
    errors[1] = validatePassword()
    return errors
  }

  function messageError(message) {
    enqueueSnackbar(message, {variant: "error"})
  }

  function messageSuccess(message) {
    enqueueSnackbar(message, {variant: "success"})
  }

  async function handleSubmit(event) {
    event.preventDefault();

    const response = await api.post("http://127.0.0.1:8000/user/login", {
      email: email, password: password
    })

    if (response.data.status) {
      set_token(response.data.data.token)
      set_id(response.data.data.id)
      set_username(response.data.data.username)
      set_email(response.data.data.email)
      set_role(response.data.data.role)
      messageSuccess(response.data.message)
      if (response.data.data.role === 'client') {
        navigate('/home')
      } else if (response.data.data.role === 'admin') {
        navigate('/panel')
      }
    } else {
      messageError(response.data.message)
    }
  }

  const errors = getErrors()

  const hasErrors = errors.some((item) => item !== "")

  return (
    <div className="login-page">
      <form className="login-form" onSubmit={handleSubmit}>
      <h2>Login</h2>
      
      <input
        className="login-input"
        type="text"
        placeholder="E-mail"
        value={email || ""}
        onChange={(e) => setEmail(e.target.value)}
      ></input>

      <input
        className="login-input"
        type="password"
        placeholder="Senha"
        value={password || ""}
        onChange={(e) => setPassword(e.target.value)}
      ></input>

      <button
        className="login-button"
        type="submit" 
        disabled={hasErrors}>
        Login
      </button>

      <div>Ainda não tem uma conta? <Link to="/register">Registre-se</Link></div>
    </form>
    </div>
  )
}

export default Login;
import React, { useState } from "react";
import { redirect, useParams, useNavigate, Link } from "react-router-dom";
import { useSnackbar } from 'notistack';

import { validateEmail, validatePassword } from "../../services/validateFields";
import { set_token, set_email, set_username } from "../../services/auth";
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

    // const response = await api.post("http://172.0.0.1:8000/user/login", {
    //   email: email, password: password
    // })

    //isso deve morrer depois
    const response = {
      data: {
        status: true,
        message: "Sucessamente",
        data: {
          token: "token",
          email: email,
          username: "nome_teste"
        }
      }
    }

    if (response.data.status) {
      set_token(response.data.data.token)
      set_email(response.data.data.email)
      set_username(response.data.data.username)
      messageSuccess(response.data.message)
      navigate("/home")
    } else {
      messageError("Falha ao realizar login.")
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
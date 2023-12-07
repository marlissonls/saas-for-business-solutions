import { redirect, useParams, useNavigate } from "react-router-dom";
import React, { useState } from "react";
import { useSnackbar } from 'notistack';

import { set_token, set_email, set_username } from "../../services/auth";
import api from "../../services/api";

function Login(props) {

  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")

  const { enqueueSnackbar } = useSnackbar()

  const navigate = useNavigate()

  function validateEmail() {
    let message = ""
    if (email.length > 10) message = "Email bigger"
    return message
  }

  function validatePassword() {
    let message = ""
    if (password.length < 5) message = "Password smaller"
    return message
  }

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

    // const response = await api.post("/login", {
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
    <form className="login-form" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="E-mail"
        value={email || ""}
        onChange={(e) => setEmail(e.target.value)}
      ></input>

      <input
        type="password"
        placeholder="Senha"
        value={password || ""}
        onChange={(e) => setPassword(e.target.value)}
      ></input>

      <button type="submit" disabled={hasErrors}>
        Login
      </button>
    </form>
  )
}

export default Login;

// <Paper elevation={3} sx={{display: "flex", flexDirection: "column", gap: "10px", padding: "10px", width: "50%"}}>
//   <TextField 
//     id="outlined-basic" 
//     label="E-mail" 
//     variant="outlined" 
//     value={email} 
//     onChange = {(e) => setEmail(e.target.value)}
//     helperText={errors[0]}
//     error={errors[0] !== ""}
//   />
//   <TextField
//     id="outlined-password-input"
//     label="Password"
//     type="password"
//     autoComplete="current-password"
//     value={password}
//     onChange = {(e) => setPassword(e.target.value)}
//     helperText={errors[1]}
//     error={errors[1] !== ""}
//   />
//   <Button variant="outlined" disabled = {hasErrors} onClick = {handleSubmit}>Login</Button>
// </Paper>
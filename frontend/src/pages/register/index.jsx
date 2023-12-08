import React, { useState } from "react";
import { useParams, useNavigate, Link } from "react-router-dom";
import { useSnackbar } from 'notistack';

import { validateName, validateEmail, validatePassword } from "../../services/validateFields";
import api from "../../services/api";

function Register(props) {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('')
  const [profileImage, setProfileImage] = useState(null);

  const { enqueueSnackbar } = useSnackbar()

  const navigate = useNavigate()

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setProfileImage(file);
  };

  function getErrors() {
    const errors = []
    errors[0] = validateName(name)
    errors[1] = validateEmail(email)
    errors[2] = validatePassword(password)
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

    const formData = new FormData();
    formData.append('name', name);
    formData.append('email', email);
    formData.append('password', password)
    formData.append('profile_image', profileImage);

    const response = await api.post("http://172.0.0.1:8000/user/register", formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });


    //isso deve morrer depois
    // const response = {
    //   data: {
    //     status: true,
    //     message: "Sucessamente",
    //     data: {
    //       token: "token",
    //       email: email,
    //       username: "nome_teste"
    //     }
    //   }
    // }

    if (response.data.status) {
      messageSuccess(response.data.message)
      navigate("/login")
    } else {
      messageError("Falha ao cadastrar usuário.")
    }
  }

  const errors = getErrors()

  const hasErrors = errors.some((item) => item !== "")

  return (
    <div className="login-page">
      <form className="login-form" onSubmit={handleSubmit}>
        <h2>Cadastrar</h2>

        <input
            className="login-input"
            type="text"
            placeholder="Nome"
            value={name || ""}
            onChange={(e) => setName(e.target.value)}
        />

        <input
            className="login-input"
            type="text"
            placeholder="E-mail"
            value={email || ""}
            onChange={(e) => setEmail(e.target.value)}
        />

        <input
            className="login-input"
            type="password"
            placeholder="Senha"
            value={password || ""}
            onChange={(e) => setPassword(e.target.value)}
        />

        <input type="file" onChange={handleFileChange} />

        <button
            className="login-button"
            type="submit" 
            disabled={hasErrors}>
            Cadastre-se
        </button>

        <div>Já tem uma conta? <Link to="/login">Faça Login</Link></div>
      </form>
    </div>
  )
}

export default Register;
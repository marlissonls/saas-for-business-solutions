import React, { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useSnackbar } from 'notistack';

import { validateName, validateEmail, validatePassword } from "../../services/validateFields";
import api from "../../services/api";

function Register(props) {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [profileImage, setProfileImage] = useState(null);
  const [selectedFileName, setSelectedFileName] = useState('');

  const { enqueueSnackbar } = useSnackbar();

  const navigate = useNavigate();

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setProfileImage(file);
    setSelectedFileName(file ? file.name : '');
  };

  function getErrors() {
    const errors = [];
    errors[0] = validateName(name);
    errors[1] = validateEmail(email);
    errors[2] = validatePassword(password);
    return errors;
  }

  function messageError(message) {
    enqueueSnackbar(message, { variant: "error" });
  }

  function messageSuccess(message) {
    enqueueSnackbar(message, { variant: "success" });
  }

  async function handleSubmit(event) {
    event.preventDefault();

    const formData = new FormData();
    formData.append('name', name);
    formData.append('email', email);
    formData.append('password', password);
    formData.append('profile_image', profileImage);

    const response = await api.post("http://127.0.0.1:8000/user/register", formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });

    if (response.data.status) {
      messageSuccess(response.data.message);
      navigate("/login");
    } else {
      messageError(response.data.message);
    }
  }

  const errors = getErrors();
  const hasErrors = errors.some((item) => item !== '');

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
        {errors[0] && <div className="error-message">{errors[0]}</div>}

        <input
          className="login-input"
          type="text"
          placeholder="E-mail"
          value={email || ""}
          onChange={(e) => setEmail(e.target.value)}
        />
        {errors[1] && <div className="error-message">{errors[1]}</div>}

        <input
          className="login-input"
          type="password"
          placeholder="Senha"
          value={password || ""}
          onChange={(e) => setPassword(e.target.value)}
        />
        {errors[2] && <div className="error-message">{errors[2]}</div>}

        <input
          type="file"
          id="profile-input"
          accept="image/*"
          onChange={handleFileChange}
          style={{ display: 'none' }}
        />

        <label htmlFor="profile-input" className="input-image">
          {selectedFileName.substring(0,22) || 'Escolher arquivo'}
        </label>

        <button
          className="login-button"
          type="submit"
          disabled={hasErrors}
        >
          Cadastre-se
        </button>

        <div>Já fez o seu cadastro? <Link to="/login">Entre</Link></div>
      </form>
    </div>
  );
}

export default Register;
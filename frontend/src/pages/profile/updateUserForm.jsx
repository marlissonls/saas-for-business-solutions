import { useState } from "react";
import { useSnackbar } from 'notistack';
import api from "../../services/api";
import { get_id, set_username, set_email, set_position } from "../../services/auth";
import { validateName, validateEmail, validatePosition, validatePassword } from "../../services/validateFields";
//import AreYouSureModal from "../../components/areYouSureModal";

function UpdateUserForm(props) {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [position, setPosition] = useState('');
  const [password, setPassword] = useState('');
  const [profileImage, setProfileImage] = useState(undefined);
  const [selectedFileName, setSelectedFileName] = useState('');
  //const [isModalVisible, setIsModalVisible] = useState(false);

  const { enqueueSnackbar } = useSnackbar();

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setProfileImage(file);
    setSelectedFileName(file ? file.name : '');
  };

  function getErrors() {
    const errors = [];
    errors[0] = validateName(name);
    errors[1] = validateEmail(email);
    errors[2] = validatePosition(position)
    errors[3] = validatePassword(password);
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
    formData.append('position', position);
    formData.append('password', password);
    formData.append('profile_image', profileImage !== undefined ? profileImage : '');

    const response = await api.put(`http://127.0.0.1:8000/user/${get_id()}`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
    
    if (response.data.status) {
      set_username(response.data.data.name)
      set_email(response.data.data.email)
      set_position(response.data.data.position)
      messageSuccess(response.data.message);
    } else {
      messageError(response.data.message);
    }
  }

  const errors = getErrors();
  const hasErrors = errors.some((item) => item !== '');

  return <>
    <form className='update-user-form' onSubmit={handleSubmit}>
      <input
        className="input"
        type="text"
        placeholder="Nome"
        value={name || ""}
        onChange={(e) => setName(e.target.value)}
      />
      
      <input
        className="input"
        type="text"
        placeholder="E-mail"
        value={email || ""}
        onChange={(e) => setEmail(e.target.value)}
      />
      
      <input
        className="input"
        type="text"
        placeholder="Cargo"
        value={position || ""}
        onChange={(e) => setPosition(e.target.value)}
      />

      <input
        className="input"
        type="password"
        placeholder="Senha"
        value={password || ""}
        onChange={(e) => setPassword(e.target.value)}
      />

      <input
        type="file"
        id="profile-input"
        accept="image/*"
        onChange={handleFileChange}
        style={{ display: 'none' }}
      />

      <label className="button select-file-btn" htmlFor="profile-input">
        {selectedFileName.substring(0,30) || 'Escolher foto de perfil'}
      </label>
    
      <div>
        <button 
          className='button submit-button' 
          type='submit'
          disabled={hasErrors}
        >
          Enviar
        </button>
      </div>
      
      {errors[0] && <div className="error-message">{errors[0]}</div> || 
      errors[1] && <div className="error-message">{errors[1]}</div> ||
      errors[2] && <div className="error-message">{errors[2]}</div> ||
      errors[3] && <div className="error-message">{errors[3]}</div>}
    </form>
  </>
}

export default UpdateUserForm;
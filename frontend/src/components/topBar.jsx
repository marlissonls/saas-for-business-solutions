import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useSnackbar } from "notistack";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faEdit, faSignOut, faTrash} from '@fortawesome/free-solid-svg-icons';
import { get_photo_url, get_id, get_username, get_email, get_company, get_position, logout, 
  set_username, set_email, set_position } from '../services/auth';
import { validateName, validateEmail, validatePosition, validatePassword } from "../services/validateFields";
import api from "../services/api";
import HOST_API from "../services/apiUrl";

function TopBar(props) {

  const { enqueueSnackbar } = useSnackbar();

  function messageError(message) {
    enqueueSnackbar(message, { variant: "error", style: {fontFamily: 'Arial'} });
  }

  function messageSuccess(message) {
    enqueueSnackbar(message, { variant: "success", style: {fontFamily: 'Arial'} });
  }

  /////////////////////////////
  // HANDLE MODAL CHANGING

  const [isProfileCardVisible, setIsProfileCardVisible] = useState(false);
  const [isProfileDataVisible, setIsProfileDataVisible] = useState(true);
  const [isUpdateProfileVisible, setIsUpdateProfileVisible] = useState(false);
  const [isDeleteProfileCardVisible, setIsDeleteProfileCardVisible] = useState(false);

  const handleProfileModal = () => {
    if (isProfileCardVisible) {
      setIsProfileCardVisible(false)
    } else {
      setIsProfileCardVisible(true)
    }
  }

  const handleProfileDataCard = () => {
    if (isProfileDataVisible) {
      setIsProfileDataVisible(false)
    } else {
      setIsProfileDataVisible(true)
    }
  }

  const handleUpdateProfileCard = () => {
    if (isUpdateProfileVisible) {
      setIsUpdateProfileVisible (false)
    } else {
      setIsUpdateProfileVisible (true)
    }
  }

  const handleDeleteProfileCard = () => {
    if (isDeleteProfileCardVisible) {
      setIsDeleteProfileCardVisible (false)
    } else {
      setIsDeleteProfileCardVisible (true)
    }
  }

  /////////////////////////////
  // SHOW PROFILE DATA
  
  const [photo, setPhoto] = useState('');
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [position, setPosition] = useState('');
  const [company, setCompany] = useState('');

  useEffect(() => {
    setPhoto(`${HOST_API}${get_photo_url()}`);
    setUsername(get_username());
    setEmail(get_email());
    setPosition(get_position());
    setCompany(get_company());
  }, []);

  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/');
  };

  /////////////////////////////
  // SHOW UPDATE PROFILE FORM

  const [updateUsername, setUpdateUsername] = useState('');
  const [updateEmail, setUpdateEmail] = useState('');
  const [updatePosition, setUpdatePosition] = useState('');
  const [updatePassword, setUpdatePassword] = useState('');
  const [updatePhoto, setUpdatePhoto] = useState(undefined);
  const [selectedFileName, setSelectedFileName] = useState('');

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    setUpdatePhoto(file);
    setSelectedFileName(file ? file.name : '');
  };

  function getErrors() {
    const errors = [];
    errors[0] = validateName(updateUsername);
    errors[1] = validateEmail(updateEmail);
    errors[2] = validatePosition(updatePosition)
    errors[3] = validatePassword(updatePassword);
    return errors;
  }

  async function handleSubmit(event) {
    event.preventDefault();

    const formData = new FormData();
    formData.append('name', updateUsername);
    formData.append('email', updateEmail);
    formData.append('position', updatePosition);
    formData.append('password', updatePassword);
    formData.append('profile_image', updatePhoto !== undefined ? updatePhoto : '');

    const response = await api.put(`/user/${get_id()}`, formData, {
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

  /////////////////////////////
  // DELETE ACCOUNT

  async function handleDeleteProfile() {
    const response = await api.delete(`/user/${get_id()}`)

    if (response.data.status) {
      messageSuccess(response.data.message)
      logout()
      navigate('/')
    } else {
      messageError(response.data.message);
    }
  }

  /////////////////////////////

  return <div className='topbar'>
    <div className='logo'>
      SmartAvalia
    </div>

    <img
      src={photo}
      className='photo-topbar'
      alt='Profile'
      onClick={handleProfileModal}
    />

    {isProfileCardVisible && <div className='profile-container-topbar'>

      {isProfileDataVisible && <div className='profile-data-topbar'>
        <p className='username-topbar'>{`Olá, ${username.split(' ')[0]}`}</p>
        <p className='email-topbar'>{email}</p>
        <p className='position-topbar'>{position !== 'null' ? position : 'Cargo a definir'}</p>
        <div 
          className='profile-action'
          onClick={() => {handleProfileDataCard(); handleUpdateProfileCard()}}
        >
          <div className='topbar-icon-box'><FontAwesomeIcon icon={faEdit} size='lg' /></div>
          Atualizar Dados
        </div>
        <div className='profile-action' onClick={handleLogout}>
          <div className='topbar-icon-box'><FontAwesomeIcon icon={faSignOut} size='lg' /></div>
          Sair
        </div>
        <div className='profile-action' onClick={() => {handleProfileDataCard(); handleDeleteProfileCard()}}>
          <div className='topbar-icon-box'><FontAwesomeIcon icon={faTrash} size='lg' /></div>
          Deletar conta
        </div>
      </div>}

      {isUpdateProfileVisible && <form className='user-form' onSubmit={handleSubmit}>
        <h3 className='form-title'>Atualizar dados</h3>

        <input
          className="input"
          type="text"
          placeholder="Nome"
          value={updateUsername || ""}
          onChange={(e) => setUpdateUsername(e.target.value)}
        />
        
        <input
          className="input"
          type="text"
          placeholder="E-mail"
          value={updateEmail || ""}
          onChange={(e) => setUpdateEmail(e.target.value)}
        />
        
        <input
          className="input"
          type="text"
          placeholder="Cargo"
          value={updatePosition || ""}
          onChange={(e) => setUpdatePosition(e.target.value)}
        />

        <input
          className="input"
          type="password"
          placeholder="Senha"
          value={updatePassword || ""}
          onChange={(e) => setUpdatePassword(e.target.value)}
        />

        <input
          type="file"
          id="profile-input"
          accept="image/*"
          onChange={handleFileChange}
          style={{ display: 'none' }}
        />

        <label className="select-file-btn" htmlFor="profile-input">
          {selectedFileName.substring(0,25) || 'Atualizar foto de perfil'}
        </label>
      
        <div className='button-container'>
          <button 
            className='button submit-button' 
            type='submit'
            disabled={hasErrors || (updateUsername === '' && updateEmail === '' && updatePosition === '' && updatePassword === '' && selectedFileName === '')}
          >
            Atualizar
          </button>

          <button
            className='button return-button'
            onClick={() => {handleUpdateProfileCard(); handleProfileDataCard()}}
          >
            Cancelar
          </button>
        </div>
        
        {errors[0] && <div className="error-message">{errors[0]}</div> || 
        errors[1] && <div className="error-message">{errors[1]}</div> ||
        errors[2] && <div className="error-message">{errors[2]}</div> ||
        errors[3] && <div className="error-message">{errors[3]}</div> ||
        (updateUsername === '' && updateEmail === '' && updatePosition === '' && updatePassword === '' && selectedFileName === '') && <div className="error-message">Todos os campos vazios</div>}
      </form>}

      {isDeleteProfileCardVisible && <div className='user-form'>
        <h3 className='form-title'>Deletar conta?</h3>

        <div className='button-container'>
          <button 
            className='button submit-button' 
            onClick={handleDeleteProfile}
          >
            Sim
          </button>

          <button
            className='button return-button'
            onClick={() => {handleDeleteProfileCard(); handleProfileDataCard()}}
          >
            Cancelar
          </button>
        </div>
      </div>}
    </div>}
  </div>
}

export default TopBar;
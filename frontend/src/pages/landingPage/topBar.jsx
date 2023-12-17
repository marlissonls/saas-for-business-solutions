import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useSnackbar } from "notistack";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser} from '@fortawesome/free-solid-svg-icons';
import { set_token, set_id, set_company, set_role, set_profile_url, set_username, set_email, set_position } from '../../services/auth';
import { validateName, validateEmail, validatePassword } from "../../services/validateFields";
import api from "../../services/api";


function TopBar(props) {

  const { enqueueSnackbar } = useSnackbar();

  function messageError(message) {
    enqueueSnackbar(message, { variant: "error" });
  }

  function messageSuccess(message) {
    enqueueSnackbar(message, { variant: "success" });
  }

  /////////////////////////////
  // HANDLE MODAL CHANGING

  const [isFormCardVisible, setIsFormCardVisible] = useState(false);
  const [isLoginFormVisible, setIsLoginFormVisible] = useState(true);
  const [isRegisterFormVisible, setIsRegisterFormVisible] = useState(false);

  const handleProfileModal = () => {
    if (isFormCardVisible) {
      setIsFormCardVisible(false)
    } else {
      setIsFormCardVisible(true)
    }
  }

  const handleLoginForm = () => {
    if (isLoginFormVisible) {
      setIsLoginFormVisible(false)
    } else {
      setIsLoginFormVisible(true)
    }
  }

  const handleResgiterForm = () => {
    if (isRegisterFormVisible) {
      setIsRegisterFormVisible (false)
    } else {
      setIsRegisterFormVisible (true)
    }
  }

  /////////////////////////////
  // SHOW LOGIN FORM

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  function getLoginInputErrors() {
    const errors = []
    errors[0] = validateEmail(email)
    errors[1] = validatePassword(password)
    return errors
  }

  const loginErrors = getLoginInputErrors()
  const hasLoginErrors = loginErrors.some((item) => item !== "")

  const navigate = useNavigate();

  async function handleLoginSubmit(e) {
    e.preventDefault();

    const response = await api.post('http://127.0.0.1:8000/user/login', {
      email: email, password: password
    })

    if (response.data.status) {
      set_token(response.data.data.token)
      set_id(response.data.data.id)
      set_username(response.data.data.username)
      set_email(response.data.data.email)
      set_position(response.data.data.position)
      set_company(response.data.data.company_name)
      set_role(response.data.data.role)
      set_profile_url(response.data.data.image_url)
      messageSuccess(response.data.message)
      if (response.data.data.role == 'client') {
        navigate('/home')
      } else {
        navigate('/panel')
      }
    } else {
      messageError(response.data.message)
    }
  }

  /////////////////////////////
  // SHOW REGISTER USER FORM

  const [username, setUsername] = useState('');
  const [registerEmail, setRegisterEmail] = useState('');
  const [registerPassword, setRegisterPassword] = useState('');
  const [photo, setPhoto] = useState(undefined);
  const [selectedFileName, setSelectedFileName] = useState('');

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    setPhoto(file);
    setSelectedFileName(file ? file.name : '');
  };

  function getRegisterInputErrors() {
    const errors = [];
    errors[0] = validateName(username);
    errors[1] = validateEmail(registerEmail);
    errors[2] = validatePassword(registerPassword);
    return errors;
  }
  
  const regiterErrors = getRegisterInputErrors();
  const hasRegisterErrors = regiterErrors.some((item) => item !== '');

  async function handleRegisterSubmit(e) {
    e.preventDefault();

    const formData = new FormData();
    formData.append('name', username);
    formData.append('email', registerEmail);
    formData.append('password', registerPassword);
    formData.append('profile_image', photo !== undefined ? photo : '');

    const response = await api.post(`http://127.0.0.1:8000/user/register`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })

    if (response.data.status) {
      messageSuccess(response.data.message);
      handleResgiterForm()
      handleLoginForm();
    } else {
      messageError(response.data.message);
    }
  }

  /////////////////////////////

  return <div className='topbar'>
    <div className='logo'>
      Insight
    </div>

    <div
      className='user-topbar'
      onClick={handleProfileModal}
      alt='Profile'
    >
      <FontAwesomeIcon icon={faUser} size='2xl' />
    </div>

    {isFormCardVisible && <div className='profile-container-topbar'>

      {isLoginFormVisible && <form className='user-form' onSubmit={handleLoginSubmit}>
        <h3 className='form-title'>Entre</h3>

        <input
          className="input"
          type="text"
          placeholder="E-mail"
          value={email || ""}
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          className="input"
          type="password"
          placeholder="Senha"
          value={password || ""}
          onChange={(e) => setPassword(e.target.value)}
        />

        <div className='button-container'>
          <button
            className='button submit-button'
            type="submit" 
            disabled={hasLoginErrors || email === '' || password === ''}>
            Entrar
          </button>

          <button
            className='button return-button'
            onClick={() => {handleLoginForm(); handleResgiterForm()}}
          >
            Cadastre-se
          </button>
        </div>

        {loginErrors[0] && <div className="error-message">{loginErrors[0]}</div> || 
        loginErrors[1] && <div className="error-message">{loginErrors[1]}</div> ||
        (email === '' || password === '') && <div className="error-message">Há campos vazios</div>}
      </form>}

      {isRegisterFormVisible && <form className='user-form' onSubmit={handleRegisterSubmit}>
        <h3 className='form-title'>Cadaster-se</h3>

        <input
          className="input"
          type="text"
          placeholder="Nome"
          value={username || ""}
          onChange={(e) => setUsername(e.target.value)}
        />
        
        <input
          className="input"
          type="text"
          placeholder="E-mail"
          value={registerEmail || ""}
          onChange={(e) => setRegisterEmail(e.target.value)}
        />

        <input
          className="input"
          type="password"
          placeholder="Senha"
          value={registerPassword || ""}
          onChange={(e) => setRegisterPassword(e.target.value)}
        />

        <input
          type="file"
          id="profile-input"
          accept="image/*"
          onChange={handleFileChange}
          style={{ display: 'none' }}
        />

        <label className="select-file-btn" htmlFor="profile-input">
          {selectedFileName.substring(0,25) || 'Escolher foto de perfil'}
        </label>
      
        <div className='button-container'>
          <button 
            className='button submit-button' 
            type='submit'
            disabled={hasRegisterErrors || username === '' || registerEmail === '' || registerPassword === '' || selectedFileName === ''}
          >
            Registrar
          </button>
          <button
            className='button return-button'
            onClick={() => {handleResgiterForm(); handleLoginForm()}}
          >
            Entre
          </button>
        </div>
        
        {regiterErrors[0] && <div className="error-message">{regiterErrors[0]}</div> || 
        regiterErrors[1] && <div className="error-message">{regiterErrors[1]}</div> ||
        regiterErrors[2] && <div className="error-message">{regiterErrors[2]}</div> ||
        (username === '' || registerEmail === '' || registerPassword === '' || selectedFileName === '') && <div className="error-message">Há campos vazios</div>}
      </form>}
    </div>}
  </div>
}

export default TopBar;
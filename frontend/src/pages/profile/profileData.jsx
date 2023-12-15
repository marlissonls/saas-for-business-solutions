import { useState, useEffect } from 'react';
import { useSnackbar } from 'notistack';
import { get_profile_url, get_id, get_username, get_position, get_email, get_company, logout } from '../../services/auth';
import api from '../../services/api';
import { useNavigate } from 'react-router-dom';
//import AreYouSureModal from '../../components/areYouSureModal';

function ProfileData(props) {
  const [profileImage, setProfileImage] = useState('');
  const [username, setUserName] = useState('');
  const [position, setPosition] = useState('');
  const [email, setEmail] = useState('');
  const [company, setCompany] = useState('');
  //const [isModalVisible, setIsModalVisible] = useState(false);

  useEffect(() => {
    setProfileImage(`http://127.0.0.1:8000${get_profile_url()}`);
    setUserName(get_username());
    setPosition(get_position());
    setEmail(get_email());
    setCompany(get_company());
  }, []);

  // const handleOpenModal = () => {
  //   setIsModalVisible(true);
  // }

  const navigate = useNavigate()

  const { enqueueSnackbar } = useSnackbar();

  function messageError(message) {
    enqueueSnackbar(message, { variant: "error" });
  }

  function messageSuccess(message) {
    enqueueSnackbar(message, { variant: "success" });
  }

  async function handleDeleteProfile() {
    const response = await api.delete(`http://127.0.0.1:8000/user/${get_id()}`)

    if (response.data.status) {
      messageSuccess(response.data.message)
      logout()
      navigate('/register')
    } else {
      messageError(response.data.message);
    }
  }

  return <div className='profile-card'>
    <img className='profile-photo' src={profileImage} alt='Profile' />
    <div>
      <p className='profile-username'>{username}</p>
      <p className='profile-position'>{`Email: ${email}`}</p>
      <p className='profile-position'>{company !== 'null' ? `Empresa: ${company}` : 'Empresa não definida'}</p>
      <p className='profile-position'>{position !== 'null' ? `Cargo: ${position}` : 'Cargo não definido'}</p>
    </div>
    <button className='button delete-button' onClick={handleDeleteProfile}>Deletar Perfil</button>
  </div>
}

export default ProfileData;
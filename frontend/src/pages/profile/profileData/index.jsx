import React, { useState, useEffect } from 'react';
import { get_id, get_profile_url, get_username, get_position, get_email, get_company } from '../../../services/auth';
import api from '../../../services/api';

function ProfileData(props) {
  const [profileImage, setProfileImage] = useState('');
  const [username, setUserName] = useState('');
  const [position, setPosition] = useState('');
  const [email, setEmail] = useState('');
  const [company, setCompany] = useState('');
  const [isModalVisible, setIsModalVisible] = useState(false);
  const [inputUsername, setInputUsername] = useState(null);
  const [inputEmail, setInputEmail] = useState(null);
  const [inputPassword, setInputPassword] = useState(null);

  useEffect(() => {
    setProfileImage(`http://127.0.0.1:8000${get_profile_url()}`);
    setUserName(get_username());
    setPosition(get_position());
    setEmail(get_email());
    setCompany(get_company());
  }, []);

  const handleOpenModal = () => {
    setIsModalVisible(true);
  }

  const handleCloseModal = () => {
    setIsModalVisible(false);
  }

  async function handleSubmit(event) {
    event.preventDefault();

    setInputUsername('Marlisson L. da Silva')

    const response = await api.put(`http://127.0.0.1:8000/user/${get_id()}`, {
      username: inputUsername, email: inputEmail, password: inputPassword
    })

    if (response.data.status) {
      response.data.message //fazer algo
    }
  }

  return <>
    <div className='profile-container'>
      <div>
        <p className='profile-username'>{username}</p>
        <p className='profile-position'>{`Email: ${email}`}</p>
        <p className='profile-position'>{company ? `Empresa: ${company}` : 'Empresa não definida'}</p>
        <p className='profile-position'>{position ? `Cargo: ${position}` : 'Cargo não definido'}</p>
      </div>
      <img className='profile-photo' src={profileImage} alt='Profile' />
    </div>
    {isModalVisible && <div className='update-profile-modal'>
      <form className='update-profile-form' onSubmit={handleSubmit}>
        <input type="text" placeholder='Nome' />
        <input type="text" placeholder='Email' />
        <input type="password" placeholder='Senha'/>
        <div>
          <button type='submit' onClick={''}>Enviar</button>
          <button onClick={handleCloseModal}>Cancelar</button>
        </div>
      </form>
    </div>}
    <div className='modal-button-container'>
      <button className='update-profile-btn' onClick={handleOpenModal}>Atualizar Perfil</button>
      <button className='delete-profile-btn'>Deletar Perfil</button>
    </div>
  </>
}

export default ProfileData;

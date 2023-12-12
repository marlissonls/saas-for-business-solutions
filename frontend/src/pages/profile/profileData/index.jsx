import React, { useState, useEffect } from 'react';
import { get_profile_url, get_username, get_email } from '../../../services/auth';

function ProfileData(props) {
  const [profileImage, setProfileImage] = useState('');
  const [userName, setUserName] = useState('');
  const [email, setEmail] = useState('');

  useEffect(() => {
    setProfileImage(`http://127.0.0.1:8000${get_profile_url()}`);
    setUserName(get_username());
    setEmail(get_email());
  }, []);

  return (
    <div>
      <div className='profile-container'>
        <img src={profileImage} className='profile-photo' alt='Profile' />
      </div>
      <div>
        <p>{userName}</p>
      </div>
      <div>
        <p>{email}</p>
      </div>
    </div>
  );
}

export default ProfileData;

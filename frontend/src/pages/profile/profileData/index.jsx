import React from 'react';
import { useState, useEffect } from 'react';
import { get_profile_url } from '../../../services/auth';

function ProfileData(props) {
  const [profileImage, setProfileImage] = useState('')
  
  useEffect(() => {
      setProfileImage(`http://127.0.0.1:8000${get_profile_url()}`)
  }, [])
  
  
  return <div>
    <img src={profileImage} />
  </div>
}

export default ProfileData;
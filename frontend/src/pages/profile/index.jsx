import { useState } from 'react';

import SideBar from '../../components/sideBar';
import MainContent from '../../containers/mainContent';
import ProfileData from './profileData';
import UpdateUserForm from './updateUserForm';

function Profile(props) {    
  return <div className='body'>
    <SideBar />
    <MainContent>
      <div className='profile-container'>
        <ProfileData />
        <UpdateUserForm />
      </div>
    </MainContent>
  </div>
}

export default Profile;
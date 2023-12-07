import React from 'react';

import SideBar from '../../components/sideBar';
import MainContent from '../../components/mainContent';
import ProfileData from './profileData';

function Profile(props) {
    
  return <div className='body'>
    <SideBar />
    <MainContent>
      <ProfileData />
    </MainContent>
  </div>
}

export default Profile;
import React from "react";

import SideBar from '../../components/sideBar';
import MainContent from '../../components/mainContent';

function Home(props) {
  return <div className='body'>
    <SideBar />
    <MainContent />
  </div>
}

export default Home;
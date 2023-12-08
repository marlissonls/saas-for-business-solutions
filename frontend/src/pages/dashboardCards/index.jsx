import React from 'react';

import SideBar from '../../components/sideBar';
import MainContent from '../../components/mainContent';
import DashCardContainer from "./dashCardContainer";

function DashboardCards(props) {
  return <div className='body'>
    <SideBar />
    <MainContent>
      <DashCardContainer />
    </MainContent>
  </div>
}

export default DashboardCards;
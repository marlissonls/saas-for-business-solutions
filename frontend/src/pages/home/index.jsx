import React from "react";

import SideBar from '../../components/sideBar';
import MainContent from '../../components/mainContent';
import CompanyData from './company';

function Home(props) {
  const data = { 
    'companyName': 'Americanas',
    'area': 'Supermercado',
    'localization': 'Rue de Paradise'
  }
  
  return <div className='body'>
    <SideBar />
    <MainContent>
      <CompanyData { ...data } />
    </MainContent>
  </div>
}

export default Home;
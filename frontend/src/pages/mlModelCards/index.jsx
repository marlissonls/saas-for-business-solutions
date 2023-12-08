import React from "react";

import SideBar from '../../components/sideBar';
import MainContent from '../../components/mainContent';
import ModelCardContainer from "./modelCardContainer";

function MlModelCards(props) {
  return <div className='body'>
    <SideBar />
    <MainContent>
      <ModelCardContainer />
    </MainContent>
  </div>
}

export default MlModelCards
import AppBar from "../../components/appBar"

import SideBar from '../../components/sideBar';
import MainContent from '../../components/mainContent';

function DashboardCards(props) {
  return <div className='body'>
    <SideBar />
    <MainContent>
      <ProfileData />
    </MainContent>
  </div>
}

export default DashboardCards
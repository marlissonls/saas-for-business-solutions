import { useParams } from "react-router-dom";

import TopBar from "../../components/topBar";
import SideBar from "../../components/sideBar";
import MainContent from "../../containers/mainContent";
import DashboardForm from "../../containers/dashboardContainer";

function Dashboard(props) {
  const { id } = useParams();

  return <div className='body'>
    <TopBar />
    <div className='display-flex'>
      <SideBar />
      <MainContent>
        <DashboardForm id={id}/>
      </MainContent>
    </div>
  </div>
}

export default Dashboard;
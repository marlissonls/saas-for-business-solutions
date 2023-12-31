import { useParams } from "react-router-dom";

import TopBar from "../../components/topBar";
import SideBar from "../../components/sideBar";
import MainContent from "../../containers/mainContent";
import MachineLearningForm from "../../containers/formContainer";

function Model(props) {
  const { id } = useParams();
 
  return <div className='body'>
    <TopBar />
    <div className='display-flex'>
      <SideBar />
      <MainContent>
        <MachineLearningForm id={id}/>
      </MainContent>
    </div>
  </div>
}

export default Model;
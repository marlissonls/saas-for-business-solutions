import TopBar from "../../components/topBar";
import SideBar from '../../components/sideBar';
import MainContent from '../../containers/mainContent';
import CompanyData from './company';

function Home(props) {
  const data = { 
    'companyName': 'Americanas',
    'area': 'Supermercado',
    'localization': 'Rue de Paradise'
  }
  
  return <div className='body'>
    <TopBar />
    <div className='display-flex'>
      <SideBar />
      <MainContent>
        <h2 className='page-title'>Empresa</h2>
        <CompanyData { ...data } />
      </MainContent>
    </div>
  </div>
}

export default Home;
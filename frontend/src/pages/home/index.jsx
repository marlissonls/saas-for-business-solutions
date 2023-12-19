import { useState, useEffect } from "react";
import TopBar from "../../components/topBar";
import SideBar from '../../components/sideBar';
import MainContent from '../../containers/mainContent';
import CompanyData from './company';
import { get_company_id } from "../../services/auth";
import api from "../../services/api";

async function getCompanyData(id) {
  const response = await api.get(`http://127.0.0.1:8000/company/${id}`)
  return response.data
}

function Home() {
  const company_id = get_company_id();
  const [data, setData] = useState(null);

  useEffect(() => {
    async function fetchCompanyData() {
      try {
        const companyData = await getCompanyData(company_id);
        setData(companyData);
      } catch (error) {
        console.error('Error fetching company data:', error);
      }
    }

    if (company_id) {
      fetchCompanyData();
    }
  }, [company_id]);

  return (
    <div className='body'>
      <TopBar />
      <div className='display-flex'>
        <SideBar />
        <MainContent>
          <h2 className='page-title'>Empresa</h2>
          {data ? <CompanyData data={data} /> : <p>Carregando dados da empresa...</p>}
        </MainContent>
      </div>
    </div>
  );
}

export default Home;
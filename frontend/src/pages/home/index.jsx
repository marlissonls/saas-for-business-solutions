import { useState, useEffect, useRef } from "react";
import { useSnackbar } from "notistack";
import TopBar from "../../components/topBar";
import SideBar from '../../components/sideBar';
import MainContent from '../../containers/mainContent';
import CompanyInfo from '../../containers/companyInfo';
import { get_company_id } from "../../services/auth";
import api from "../../services/api";


async function getCompanyData(id) {
  const response = await api.get(`http://127.0.0.1:8000/company/${id}`)
  return response.data
}

function Home() {
  const refLoading = useRef(false)
  const [data, setData] = useState(null);

  const { enqueueSnackbar } = useSnackbar();

  function messageError(message) {
    enqueueSnackbar(message, { variant: "error", style: {fontFamily: 'Arial'} });
  }

  useEffect(() => {
    async function fetchCompanyData(company_id) {
      try {
        const companyData = await getCompanyData(company_id);
        setData(companyData);
      } catch (error) {
        messageError('Erro ao carregar dados da empresa.')
      } finally {
        refLoading.current = false;
      }
    }

    const company_id = get_company_id();
    if (!refLoading.current) {
      if (company_id) {
        console.log(company_id)
        refLoading.current = true;
        fetchCompanyData(company_id);
      }
    }
  }, []);

  return (
    <div className='body'>
      <TopBar />
      <div className='display-flex'>
        <SideBar />
        <MainContent>
          <h2 className='page-title'>Empresa</h2>
          {data ? <CompanyInfo data={data} /> : <p>Carregando dados da empresa...</p>}
        </MainContent>
      </div>
    </div>
  );
}

export default Home;
import { useState, useEffect, useRef } from "react";
import { useSnackbar } from "notistack";
import TopBar from "../../components/topBar";
import SideBar from '../../components/sideBar';
import MainContent from '../../containers/mainContent';
import CompanyInfo from '../../containers/companyInfo';
import { get_company_id } from "../../services/auth";
import api from "../../services/api";


async function getCompanyData(id) {
  const response = await api.get(`/company/${id}`)
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
        const reqData = await getCompanyData(company_id);
        if (reqData.status) {
          setData(reqData.data);
        } else {
          setData(false)
        }
      } catch (error) {
        messageError('Erro ao carregar dados da empresa.')
      } finally {
        refLoading.current = false;
      }
    }

    const company_id = get_company_id();
    if (company_id == "null") return;

    if (!refLoading.current) {
      if (company_id) {
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
          <h2 className='page-title'>Sobre a SmartAvalia Avaliação Imobiliária</h2>
          <div className='company-info-body'>
            {data ? <CompanyInfo data={data} /> : <p>Carregando dados da empresa...</p>}
          </div>
        </MainContent>
      </div>
    </div>
  );
}

export default Home;
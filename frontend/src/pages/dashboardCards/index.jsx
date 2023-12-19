import { useState, useEffect } from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlus, faChartColumn, faEye, faEdit, faX} from '@fortawesome/free-solid-svg-icons';
import { Link } from 'react-router-dom';
import TopBar from '../../components/topBar';
import SideBar from '../../components/sideBar';
import MainContent from '../../containers/mainContent';
import api from '../../services/api';


function DashboardCards(props) {
  const [isCreateCardVisible, setIsCreateCardVisible] = useState(false)
  const [isCardVisible, setIsCardVisible] = useState(false)
  const [isEditFormVisible, setIsEditFormVisible] = useState(false)

  ////////////////////////////////
  // 
  // const company_id = get_company_id();
  // const [data, setData] = useState(null);

  // useEffect(() => {
  //   async function fetchCompanyData() {
  //     try {
  //       const companyData = await getCompanyData(company_id);
  //       setData(companyData);
  //     } catch (error) {
  //       console.error('Error fetching company data:', error);
  //     }
  //   }

  //   if (company_id) {
  //     fetchCompanyData();
  //   }
  // }, [company_id]);

  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const data = [
        { id: 1, name: 'Item 1', date: '10/10/2010', description: 'Descrição do Item 1' },
        { id: 2, name: 'Item 2', date: '10/10/2010', description: 'Descrição do Item 2' },
        { id: 3, name: 'Item 3', date: '10/10/2010', description: 'Descrição do Item 3' },
        { id: 4, name: 'Item 4', date: '10/10/2010', description: 'Descrição do Item 1' },
        { id: 5, name: 'Item 5', date: '10/10/2010', description: 'Descrição do Item 2' },
        { id: 6, name: 'Item 6', date: '10/10/2010', description: 'Descrição do Item 3' },
      ];
      setData(data);
    };

    fetchData();
  }, []);

  /////////////////////////////////
  // SHOW CREATE CARD MODAL

  const [createCardTitle, setCreateCardTitle] = useState('');
  const [createCardDescription, setCreateCardDescription] = useState('');

  async function handleCreateCard(e) {
    e.preventDefault();

    const formData = new FormData();
    formData.append('name', updateCardTitle);
    formData.append('description', updateCardDescription);

    const response = await api.post(`http://127.0.0.1:8000/dashboards`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })

    if (response.data.status) {
      console.log('ok')
    }
  }

  /////////////////////////////////
  // JUST SHOW A CARD

  const [cardTitle, setCardTitle] = useState('');
  const [cardDescription, setCardDescription] = useState('');

  /////////////////////////////////
  // SHOW UPDATE CARD MODAL

  const [updatingCardId, setUpdatingCardId] = useState('');
  const [updateCardTitle, setUpdateCardTitle] = useState('');
  const [updateCardDescription, setUpdateCardDescription] = useState('');

  async function handleUpdateCard(e) {
    e.preventDefault();

    const formData = new FormData();
    formData.append('name', updateCardTitle);
    formData.append('description', updateCardDescription);

    const response = await api.put(`http://127.0.0.1:8000/dashboards/${updatingCardId}`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })

    if (response.data.status) {
      console.log('ok')
    }
  }

  return <div className='body'>
    <TopBar />
    <div className='display-flex'>
    <SideBar />
    <MainContent>
      <h2 className='page-title'>Dashboards</h2>
      <button
        className='table-add-new'
        onClick={() => {
          setIsCardVisible(false);
          setIsEditFormVisible(false);
          setIsCreateCardVisible(true);
        }}
      >
        <FontAwesomeIcon icon={faPlus}  size='3x' />
      </button>
      <table className='table'>
        <thead>
          <tr className='table-title-row'>
            <th className='th table-title-col-id'>ID</th>
            <th className='th table-title-col-name'>Título</th>
            <th className='th table-title-col-data'>Data de criação</th>
            <th className='th table-title-col-action'>Ação</th>
          </tr>
        </thead>
        <tbody>
          {data.map((card, index) => (
            <tr key={index} className={`${index % 2 === 0 ? 'even-row' : 'odd-row'}`}>
              <td className='td'>{card.id}</td>
              <td className='td'>{card.name}</td>
              <td className='td'>{card.date}</td>
              <td className='td table-action-container'>
                <Link to={`/dashboards/${card.id}`}>
                  <div className='table-action-icon arrow'>
                    <FontAwesomeIcon icon={faChartColumn} size='1x' />
                  </div>
                </Link>
                <button
                  className='table-action-icon eye'
                  onClick={() => {
                    setIsCreateCardVisible(false);
                    setIsEditFormVisible(false);
                    setIsCardVisible(true);
                    setCardTitle(card.name);
                    setCardDescription(card.description);
                  }}
                >
                  <FontAwesomeIcon icon={faEye} size='1x' />
                </button>
                <button
                  className='table-action-icon edit'
                  onClick={() => {
                    setIsCreateCardVisible(false);
                    setIsCardVisible(false)
                    setIsEditFormVisible(true);
                    setUpdatingCardId(card.id);
                  }}
                >
                  <FontAwesomeIcon icon={faEdit} size='1x' />
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* SHOW CREATE CARD MODAL */}

      {isCreateCardVisible && <form className='card-form' onSubmit={handleCreateCard}>
        <h3 className='form-title'>Criar novo dashboard</h3>

        <input 
          className='input-card'
          type="text"
          placeholder='Título do dashboard'
          value={createCardTitle || ''}
          onChange={(e) => setCreateCardTitle(e.target.value)}
        />

        <textarea
          className='textarea'
          type="text"
          placeholder='Descrição do dashboard'
          value={createCardDescription || ''}
          onChange={(e) => setCreateCardDescription(e.target.value)}
        />

        <div className='button-container'>
          <button 
            className='button submit-button' 
            type='submit'
            disabled={(updateCardTitle === '' && updateCardDescription === '')}
            // disabled={hasErrors || (updateTitle === '' && updateDescription === '')}
          >
            Criar
          </button>

          <button
            className='button return-button'
            onClick={() => {
              setIsCardVisible(false);
              setIsCreateCardVisible(false);
              setIsEditFormVisible(false);
            }}
          >
            Cancelar
          </button>
        </div>
      </form>}

      {/* JUST SHOW CARD DESCRIPTION */}

      {isCardVisible && <div className='card'>
        <div className='card-title'>
          <p>{cardTitle}</p>
          <button
            className='card-close-icon'
            onClick={() => {
              setIsCardVisible(false);
              setIsCreateCardVisible(false);
              setIsEditFormVisible(false);
            }}
          >
            <FontAwesomeIcon icon={faX} />
          </button>
        </div>
        <p className='card-description'>{cardDescription}</p>
      </div>}

      {/* SHOW UPDATE CARD MODAL */}

      {isEditFormVisible && <form className='card-form' onSubmit={handleUpdateCard}>
        <h3 className='form-title'>Editar dashboard</h3>
        
        <input 
          className='input-card'
          type="text"
          placeholder='Título do dashboard'
          value={updateCardTitle || ''}
          onChange={(e) => setUpdateCardTitle(e.target.value)}
        />

        <textarea
          className='textarea'
          type="text"
          placeholder='Descrição do dashboard'
          value={updateCardDescription || ''}
          onChange={(e) => setUpdateCardDescription(e.target.value)}
        />

        <div className='button-container'>
          <button 
            className='button submit-button' 
            type='submit'
            disabled={(updateCardTitle === '' && updateCardDescription === '')}
            // disabled={hasErrors || (updateTitle === '' && updateDescription === '')}
          >
            Atualizar
          </button>

          <button
            className='button return-button'
            onClick={() => {
              setIsCardVisible(false);
              setIsCreateCardVisible(false);
              setIsEditFormVisible(false);
            }}
          >
            Cancelar
          </button>
        </div>
      </form>}
    </MainContent>
    </div>
  </div>
}

export default DashboardCards;
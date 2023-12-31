import { useState, useEffect } from 'react'
import { useSnackbar } from "notistack";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlus, faCogs, faEye, faEdit, faX} from '@fortawesome/free-solid-svg-icons';
import { Link } from 'react-router-dom';
import TopBar from '../../components/topBar';
import SideBar from '../../components/sideBar';
import MainContent from '../../containers/mainContent';
import { get_company_id } from '../../services/auth';
import { validateCardInputs } from "../../services/validateFields";
import api from '../../services/api';


async function getModelsData(id) {
  const response = await api.get(`http://127.0.0.1:8000/model?company_id=${id}`)
  return response.data.data
}

function MlModelCards(props) {

  const { enqueueSnackbar } = useSnackbar();

  function messageError(message) {
    enqueueSnackbar(message, { variant: "error" });
  }

  function messageSuccess(message) {
    enqueueSnackbar(message, { variant: "success" });
  }


  function getCardInputErrors(cardTitle, cardDescription) {
    const errors = []
    errors[0] = validateCardInputs(cardTitle)
    errors[1] = validateCardInputs(cardDescription)
    return errors
  }

  ////////////////////////////////
  // HANDLE MODAL CHANGING

  const [isCreateCardVisible, setIsCreateCardVisible] = useState(false)
  const [isCardVisible, setIsCardVisible] = useState(false)
  const [isEditFormVisible, setIsEditFormVisible] = useState(false)

  ////////////////////////////////
  // GET THE COMPANY MODELS

  const company_id = get_company_id();
  const [data, setData] = useState([]);

  useEffect(() => {
    async function fetchModelsData() {
      try {
        const modelsData = await getModelsData(company_id);
        setData(modelsData);
      } catch (error) {
        console.error('Error fetching models data:', error);
      }
    }

    if (company_id) {
      fetchModelsData();
    }
  }, [company_id]);

  /////////////////////////////////
  // SHOW CREATE CARD MODAL

  const [createCardTitle, setCreateCardTitle] = useState('');
  const [createCardDescription, setCreateCardDescription] = useState('');

  const createCardErrors = getCardInputErrors(createCardTitle, createCardDescription)
  const hasCreateCardErrors = createCardErrors.some((item) => item !== "")

  async function handleCreateCard(e) {
    e.preventDefault();

    const formData = new FormData();
    formData.append('name', createCardTitle);
    formData.append('description', createCardDescription);
    formData.append('company_id', company_id);

    const response = await api.post(`http://127.0.0.1:8000/model`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })

    if (response.data.status) {
      messageSuccess(response.data.message)
    } else {
      messageError(response.data.message)
    }

    setIsCreateCardVisible(false)
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

  const updateCardErrors = getCardInputErrors(updateCardTitle, updateCardDescription)
  const hasUpdateCardErrors = updateCardErrors.some((item) => item !== "")

  async function handleUpdateCard(e) {
    e.preventDefault();

    const formData = new FormData();
    formData.append('name', updateCardTitle);
    formData.append('description', updateCardDescription);

    const response = await api.put(`http://127.0.0.1:8000/model/${updatingCardId}`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })

    if (response.data.status) {
      messageSuccess(response.data.message)
    } else {
      messageError(response.data.message)
    }

    setIsEditFormVisible(false)
  }

  return <div className='body'>
    <TopBar />
    <div className='display-flex'>
    <SideBar />
    <MainContent>
      <h2 className='page-title'>
        Machine Learning
        <button
        className='button-add-new'
        onClick={() => {
          setIsCardVisible(false);
          setIsEditFormVisible(false);
          setIsCreateCardVisible(true);
        }}
      >
        <FontAwesomeIcon icon={faPlus}  size='2x' />
      </button>
      </h2>
      <table className='table'>
        <thead>
          <tr className='table-title-row'>
            <th className='th table-title-col-id'>ID</th>
            <th className='th table-title-col-name'>Título</th>
            <th className='th table-title-col-data'>Criado / Atualizado</th>
            <th className='th table-title-col-action'>Ação</th>
          </tr>
        </thead>
        <tbody>
          {data.map((card, index) => (
            <tr key={index} className={`${index % 2 === 0 ? 'even-row' : 'odd-row'}`}>
              <td className='td'>{card.id}</td>
              <td className='td'>{card.name}</td>
              <td className='td'>{card.date}</td>
              <td className='td'>
                <div className='table-action-container'>
                  <Link to={`/models/${card.id}`}>
                    <div className='table-action-icon arrow'>
                      <FontAwesomeIcon icon={faCogs} size='1x' />
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
                      setUpdateCardTitle(card.name);
                      setUpdateCardDescription(card.description);
                    }}
                  >
                    <FontAwesomeIcon icon={faEdit} size='1x' />
                  </button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* SHOW CREATE CARD MODAL */}

      {isCreateCardVisible && <form className='card-form' onSubmit={handleCreateCard}>
        <h3 className='form-title'>Criar novo Modelo</h3>

        <input 
          className='input-card'
          type="text"
          placeholder='Título do modelo'
          value={createCardTitle || ''}
          onChange={(e) => setCreateCardTitle(e.target.value)}
        />

        <textarea
          className='textarea'
          type="text"
          placeholder='Descrição do modelo'
          value={createCardDescription || ''}
          onChange={(e) => setCreateCardDescription(e.target.value)}
        />

        <div className='button-container'>
          <button 
            className='button submit-button' 
            type='submit'
            disabled={hasCreateCardErrors || (createCardTitle === '' || createCardDescription === '')}
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

        {hasCreateCardErrors[0] && <div className="error-message">{hasCreateCardErrors[0]}</div> || 
        hasCreateCardErrors[1] && <div className="error-message">{hasCreateCardErrors[1]}</div> ||
        (createCardTitle === '' || createCardDescription === '') && <div className="error-message">Há campos vazios</div>}
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
        <p className='card-description'>{cardDescription.split('\r\n').map((line, index) => (
          <span key={index}>
            {line}
            <br />
          </span>
        ))}</p>
      </div>}

      {/* SHOW UPDATE CARD MODAL */}

      {isEditFormVisible && <form className='card-form' onSubmit={handleUpdateCard}>
        <h3 className='form-title'>Editar modelo</h3>
        
        <input 
          className='input-card'
          type="text"
          placeholder='Título do modelo'
          value={updateCardTitle || ''}
          onChange={(e) => setUpdateCardTitle(e.target.value)}
        />

        <textarea
          className='textarea'
          type="text"
          placeholder='Descrição do modelo'
          value={updateCardDescription || ''}
          onChange={(e) => setUpdateCardDescription(e.target.value)}
        />

        <div className='button-container'>
          <button 
            className='button submit-button' 
            type='submit'
            disabled={hasUpdateCardErrors || (updateCardTitle === '' && updateCardDescription === '')}
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

        {hasUpdateCardErrors[0] && <div className="error-message">{hasUpdateCardErrors[0]}</div> || 
        hasUpdateCardErrors[1] && <div className="error-message">{hasUpdateCardErrors[1]}</div> ||
        (updateCardTitle === '' || updateCardDescription === '') && <div className="error-message">Há campos vazios</div>}
      </form>}
    </MainContent>
    </div>
  </div>
}

export default MlModelCards;
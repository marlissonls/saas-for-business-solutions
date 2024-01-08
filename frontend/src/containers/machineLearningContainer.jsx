import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faArrowUpRightFromSquare } from '@fortawesome/free-solid-svg-icons';
import api from '../services/api';

const getInitialValue = (field) => {
  switch (field.type) {
    case 'text':
    case 'email':
    case 'password':
    case 'number':
      return '';
    case 'textarea':
      return '';
    case 'select':
      return field.options && field.options.length > 0 ? field.options[0] : '';
    case 'checkbox':
      return false;
    default:
      return '';
  }
};

const getInitialFormValues = (fields) => {
  const initialFormValues = {};
  fields.forEach((field) => {
    initialFormValues[field.name] = getInitialValue(field);
  });
  return initialFormValues;
};

const MachineLearningForm = ({ id }) => {
  const [formInputs, setFormInputs] = useState([]);
  const [featuresTemplate, setFeaturesTemplate] = useState({});
  const [jupyterLink, setJupyterLink] = useState('#');
  const [formValues, setFormValues] = useState({});
  const [modelTitle, setModelTitle] = useState('');
  const [prediction, setPrediction] = useState([]);
  const [mouseState, setMouseState] = useState('default');

  useEffect(() => {
    const getFormInputs = async () => {
      try {
        const response = await api.get(`http://127.0.0.1:8000/model/${id}`)
        const features_inputs = JSON.parse(response.data.data.features_inputs);
        const features_template = JSON.parse(response.data.data.features_template);
        const jupyter_link = response.data.data.jupyter_link;

        setFormInputs(features_inputs);
        setFeaturesTemplate(features_template);
        setJupyterLink(jupyter_link);
        setModelTitle(response.data.data.name)

        // Inicializa os valores do formulário com base nos campos
        const initialFormValues = getInitialFormValues(features_inputs);
        setFormValues(initialFormValues);
      } catch (error) {
        console.error('Erro ao obter dados do formulário:', error);
      }
    };

    getFormInputs();
  }, []);

  const handleInputChange = (fieldName, value) => {
    // Atualiza o estado com os valores do formulário
    setFormValues((prevValues) => ({
      ...prevValues,
      [fieldName]: value,
    }));
  };

  async function handleSubmit(e) {
    e.preventDefault();

    setMouseState('wait');
    try {
      const response = await api.post(`http://127.0.0.1:8000/model/predict/${id}`, {
        features_values: formValues,
        features_template: featuresTemplate,
      });
  
      if (response.data.status) {
        console.log(response.data.message);
        setPrediction(response.data.data);
      } else {
        console.log(response.data.message);
      }
    } catch (error) {
      console.error('Erro ao processar a solicitação', error);
    } finally {
      // Após a conclusão, restaure o estado do mouse para 'default'
      setMouseState('default');
    }
  }
  

  const renderFormField = (field) => {
    // Lógica para renderizar o campo de acordo com o tipo
    switch (field.type) {
      case 'text':
      case 'email':
      case 'password':
      case 'number':
        return (
          <input
            type={field.type}
            id={field.name}
            name={field.name}
            value={formValues[field.name]}
            onChange={(e) => handleInputChange(field.name, e.target.value)}
          />
        );
      case 'textarea':
        return (
          <textarea
            id={field.name}
            name={field.name}
            value={formValues[field.name]}
            onChange={(e) => handleInputChange(field.name, e.target.value)}
          />
        );
      case 'checkbox':
        return (
          <input
            type="checkbox"
            id={field.name}
            name={field.name}
            checked={formValues[field.name]}
            onChange={() => handleInputChange(field.name, !formValues[field.name])}
          />
        );
      case 'select':
        return (
          <select
            id={field.name}
            name={field.name}
            value={formValues[field.name]}
            onChange={(e) => handleInputChange(field.name, e.target.value)}
          >
            {field.options.map((option) => (
              <option key={option} value={option}>
                {option.split('_')[1].replaceAll('-', ' ')}
              </option>
            ))}
          </select>
        );
      default:
        return null;
    }
  };

  const renderForm = () => {
    if (!formInputs.length) {
      return <p>Não há campos disponíveis ainda.</p>;
    }

    return (
      <form className='machine-learning-form' onSubmit={handleSubmit}>
        {formInputs.map((field) => (
          <div className={'machine-learning-field ' + field.type} key={field.name}>
            {field.type === 'checkbox' ? (
              <>
                {renderFormField(field)}
                <label htmlFor={field.name}>{field.label}</label>
              </>
            ) : (
              <>
                <label htmlFor={field.name}>{field.label}</label>
                {renderFormField(field)}
              </>
            )}
          </div>
        ))}

        <div className='button-container'>
          {formInputs.length > 0 && (<button 
              className='button submit-button'
              type="submit"
              disabled={Object.values(formValues).some(value => value === "")}
            >
              Enviar
            </button>
          )}
        </div>
        
        {Object.values(formValues).some(value => value === "") && <div className="error-message">Há campos vazios</div>}
      </form>
    );
  };

  return <>
    <h2
      className='page-title'
    >
      {modelTitle}
      <Link to={jupyterLink} target="_blank" rel="noopener noreferrer">
        <div className=''>
          <FontAwesomeIcon icon={faArrowUpRightFromSquare} size='1x' />
        </div>
      </Link>
    </h2>
    <div className='machine-learning-page' style={{ cursor: mouseState }}>
      {renderForm()}
      {prediction && prediction.length > 0 && (
        <div className='machine-learning-result'>
          <p>Estimativa de Preço</p>
          {prediction.map((pred, index) => (
            <p key={index}>{typeof pred === 'number' ? 'R$ ' + pred.toFixed(2) : pred}</p>
          ))}
        </div>
      )}
    </div>
  </>
};

export default MachineLearningForm;

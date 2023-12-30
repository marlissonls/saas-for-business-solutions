import React, { useState, useEffect } from 'react';
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
  const [formValues, setFormValues] = useState({});
  const [modelTitle, setModelTitle] = useState('');

  useEffect(() => {
    const getFormInputs = async () => {
      try {
        const response = await api.get(`http://127.0.0.1:8000/model/${id}`)
        const inputs = JSON.parse(response.data.data.features_inputs);
        const featTemplate = JSON.parse(response.data.data.features_template);
        
        setFormInputs(inputs);
        setFeaturesTemplate(featTemplate);
        setModelTitle(response.data.data.name)

        // Inicializa os valores do formulário com base nos campos
        const initialFormValues = getInitialFormValues(inputs);
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
    console.log(formValues)
    const response = await api.post(`http://127.0.0.1:8000/model/predict/${id}`, {
      features_values: formValues,
      features_template: featuresTemplate, 
    })
    
    console.log(response.data.status)
    console.log(response.data.message)
    console.log(response.data.data)
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
      <form className='model-form' onSubmit={handleSubmit}>
        {formInputs.map((field) => (
          <div className={field.type} key={field.name}>
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
        {formInputs.length > 0 && (
          <button type="submit">Enviar</button>
        )}
      </form>
    );
  };

  return (
    <div>
      <h2 className='page-title'>{modelTitle}</h2>
      {renderForm()}
    </div>
  );
};

export default MachineLearningForm;

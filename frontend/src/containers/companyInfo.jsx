import React from 'react';

function CompanyInfo({ data }) {
  const name = data.name 
  const area = data.area 
  const description = data.description 
  const localization = data.localization
  const phone = data.phone

  return <>
    <h1 className='company-welcome'>Bem-vindo(a) à empresa {name}</h1>
    <div className='company-data-container'><p className='company-label'>Setor:</p><p className='company-info'>{area}</p></div>
    <div className='company-data-container'><p className='company-label'>Descrição:</p><p className='company-info'>{description}</p></div>
    <div className='company-data-container'><p className='company-label'>Localização:</p><p className='company-info'>{localization}</p></div>
    <div className='company-data-container'><p className='company-label'>Contato:</p><p className='company-info'>{phone}</p></div>
  </>
}

export default CompanyInfo;

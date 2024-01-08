import React from 'react';

function CompanyInfo({ data }) {
  const name = data.name 
  const description = data.description 
  const localization = data.localization
  const phone = data.phone

  return <>
    <h1 className='company-welcome'>Bem-vindo(a) à {name}</h1>
    <div className='company-data-container'><p className='company-info'>{description}</p></div>
    <div className='company-data-container'><p className='company-info'>{'Estamos Localizados na ' + localization}</p></div>
    <div className='company-data-container'><p className='company-info'>{'Contato: ' + phone}</p></div>
  </>
}

export default CompanyInfo;

import React from 'react';

function CompanyInfo({ data }) {
  const name = data.name 
  const description = data.description 
  const localization = data.localization
  const phone = data.phone

  return <>
    <h1 className='company-welcome'>Bem-vindo(a) à {name}</h1>
    <p className='company-info'>{description}</p>
    <p className='company-info'>{'Estamos Localizados na ' + localization + '.'}</p>
    <p className='company-info'>{'Contato: ' + phone + '.'}</p>
  </>
}

export default CompanyInfo;

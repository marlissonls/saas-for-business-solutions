import React from 'react';

function CompanyData({ companyName, area, localization }) {
    return <div>
      <h1>Bem-vindo à {companyName}</h1>
      <p><strong>Setor:</strong> {area}</p>
      <p><strong>Localização:</strong> {localization}</p>
    </div>
}

export default CompanyData;
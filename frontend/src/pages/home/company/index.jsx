function CompanyData({ data }) {
  const name = data.data.name 
  const area = data.data.area 
  const description = data.data.description 
  const localization = data.data.localization  

  return <>
    <h1 className='company-welcome'>Bem-vindo à empresa {name}</h1>
    <div className='company-data-container'><p className='company-label'>Setor:</p><p className='company-info'>{area}</p></div>
    <div className='company-data-container'><p className='company-label'>Localização:</p><p className='company-info'>{localization}</p></div>
    <div className='company-data-container'><p className='company-label'>Descrição:</p><p className='company-info'>{description}</p></div>
  </>
}

export default CompanyData;

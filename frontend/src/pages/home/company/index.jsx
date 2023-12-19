import React, { useEffect, useState } from "react";
import { useSnackbar } from "notistack";

function CompanyData({ data }) {
  const { enqueueSnackbar } = useSnackbar();
  console.log(data)
  const [name, setName] = useState('');
  const [area, setArea] = useState('');
  const [description, setDescription] = useState('');
  const [localization, setLocalization] = useState('');

  function messageSuccess(message) {
    enqueueSnackbar(message, { variant: "success" });
  }

  useEffect(() => {
    if (data.status) {
      setName(data.data.name || '');
      setArea(data.data.area || '');
      setDescription(data.data.description || '');
      setLocalization(data.data.localization || '');
      messageSuccess(data.message);
    }
  }, [data]);

  return (<>
      <h1 className='company-welcome'>Bem-vindo à empresa {name}</h1>
      <div className='company-data-container'><p className='company-label'>Setor:</p><p className='company-info'>{area}</p></div>
      <div className='company-data-container'><p className='company-label'>Localização:</p><p className='company-info'>{localization}</p></div>
      <div className='company-data-container'><p className='company-label'>Descrição:</p><p className='company-info'>{description}</p></div>
    </>
  );
}

export default CompanyData;

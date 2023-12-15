import React from 'react';

import SideBar from '../../components/sideBar';
import MainContent from '../../containers/mainContent';
import CardContainer from "../../containers/cardContainer";

const dashboardCards = [
  { id: 'A', name: 'Dashboard Estatístico', description: 'Em linguística, a noção de texto é ampla e ainda aberta a uma definição mais precisa. Grosso modo, pode ser entendido como manifestação linguística das ideias de um autor, que serão interpretadas pelo leitor de acordo com seus conhecimentos linguísticos e culturais. Seu tamanho é variável.' },
  { id: 'B', name: 'Dashboard Medicina', description: 'O interesse pelo texto como objeto de estudo gerou vários trabalhos importantes de teóricos da Linguística Textual, que percorreram fases diversas cujas características principais eram transpor os limites da frase descontextualizada da gramática tradicional e ainda incluir os relevantes papéis do autor e do leitor na construção de textos.' },
  { id: 'C', name: 'Dashboard de Vendas', description: 'Vendas' },
  { id: 'A', name: 'Dashboard Estatístico', description: 'Estatistico' },
  { id: 'B', name: 'Dashboard Medicina', description: 'Medicina' },
  { id: 'C', name: 'Dashboard de Vendas', description: 'Vendas' }
];

function DashboardCards(props) {
  return <div className='body'>
    <SideBar />
    <MainContent>
      <h2 className='page-title'>Dashboards</h2>
      <CardContainer route='dashboards' cards={dashboardCards} />
    </MainContent>
  </div>
}

export default DashboardCards;

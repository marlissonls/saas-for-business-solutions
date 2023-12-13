import React from 'react';
import Card from '../../../components/card';

function DashCardContainer({ cards }) {
  return (<div className='card-page'>
      <h2 className='page-title'>Dashboards</h2>
      <div className='card-container'>
        {cards.map((item, index) => (
          <Card 
            key={index} 
            id={item.id} 
            title={item.name} 
            description={item.description}
          />
        ))}
      </div>
  </div>)
}

export default DashCardContainer;
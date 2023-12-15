import React from 'react';
import Card from '../components/card';

function CardContainer({ route, cards }) {
  return <div className='card-container'>
    {cards.map((item, index) => (
      <Card 
        key={index}
        route={route}
        id={item.id}
        title={item.name}
        description={item.description}
      />
    ))}
  </div>
}

export default CardContainer;
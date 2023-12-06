import React from "react";
import AppBar from "./appBar";
import PricingCards from "./pricingCards";

const cards = [{id: 1, price: 5, name: '01'}, {id: 2, price: 10, name: '02'}, {id: 3, price: 15, name: '03'}]

function LandingPage(props) {
  return (
    <>
      <AppBar />
      <div className="cards-container">{cards.map(item => <PricingCards price={item.price} name={item.name} key={item.id}/>)}</div>
    </>
  )
}

export default LandingPage;
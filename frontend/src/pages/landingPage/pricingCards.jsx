import React from "react";

function PricingCards({price, name}) {
  return <div className="pricing-cards">{price}, {name}</div>
}

export default PricingCards;
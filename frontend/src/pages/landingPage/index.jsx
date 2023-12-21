import TopBar from "./topBar";
import PricingCards from "./pricingCards";

const cards = [{id: 1, price: 5, name: '01'}, {id: 2, price: 10, name: '02'}, {id: 3, price: 15, name: '03'}]

function LandingPage(props) {
  return <div className='body'>
    <TopBar />
    <div className='hero-section'>
      Bem Vindos a Insight
    </div>
    <div className="cards-container">
      {cards.map(item => <PricingCards price={item.price} name={item.name} key={item.id} />)}
    </div>
  </div>
}

export default LandingPage;
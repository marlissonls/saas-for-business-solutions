import TopBar from "./topBar";
import PricingCards from "./pricingCards";

const cards = [{id: 1, price: 5, name: '01'}, {id: 2, price: 10, name: '02'}, {id: 3, price: 15, name: '03'}]

function LandingPage(props) {
  return <div className='body'>
    <TopBar />

    <div className='hero-section'>
      <h1>Potencialize seu negócio com a Insight!</h1>
      <p>Descomplicamos seus dados para impulsionar o sucesso do seu negócio!</p>
      <p>Visualize e analise seus dados de forma dinâmica. Solicite modelos de Machine Learning exclusivos para sua empresa.</p>
      <p>Conte conosco para transformar informações em ações estratégicas!</p>
    </div>

    <div className="cards-container">
      {cards.map(item => <PricingCards price={item.price} name={item.name} key={item.id} />)}
    </div>
  </div>
}

export default LandingPage;
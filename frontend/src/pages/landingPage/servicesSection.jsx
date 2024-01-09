function ServicesSection(props) {
  return <>
    <div className='ourservices-section'>
      <div className='section-title'>
        <div className='section-divisor'></div>
        <p>Nossos Serviços</p>
      </div>

      <div className='ourservice-cards'>
        <div className='machine-service ourservice-card'>
          <h3>Calculadora Precify</h3>
          <p>- Permite realizar estimativas de preços de imóveis de modo fácil e rápido.</p>
          <p>- Sempre atualizado seguindo as tendências e flutuações do mercado imobiliáriop.</p>
          <p>- Fornece estimativas precisas e relevantes para orientar suas decisões no mercado imobiliário.</p>
        </div>
        <div className='chart-service ourservice-card'>
          <h3>Smart BI</h3>
          <p>- Permite a visualização gráfica dos dados do modelo, facilitando a elaboração de relatórios.</p>
          <p>- Apresenta visualizações sofisticadas e envolventes para uma análise detalhada.</p>
          <p>- Apresenta gráficos dinâmicos, aprofundando a compreensão e interpretação dos dados.</p>
        </div>
      </div>
    </div>
  </>
}

export default ServicesSection;
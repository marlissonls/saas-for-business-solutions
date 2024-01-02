function ServicesSection(props) {
  return <>
    <div className='ourservices-section'>
      <div className='section-title'>
        <div className='section-divisor'></div>
        <p>Nossos Serviços</p>
      </div>

      <div className='ourservice-cards'>
        <div className='chart-service ourservice-card'>
          <h3>Descubra Insights com Visualizações Gráficas e Dinâmicas dos Dados</h3>
          <p>- Personalize suas visualizações escolhendo manualmente as variáveis relevantes.</p>
          <p>- Agrupe dados de maneira inteligente por média, soma ou quantidade.</p>
          <p>- Explore gráficos dinâmicos com opções de zoom para uma compreensão mais profunda.</p>
          <p>- Aproveite o poder da automação para otimizar processos e alcançar resultados extraordinários.</p>
        </div>
        <div className='machine-service ourservice-card'>
          <h3>Faça Previsões Assertivas com Modelos de Machine Learning Avançados dos Dados</h3>
          <p>- Solicite modelos específicos de machine learning para impulsionar estratégias únicas de crescimento.</p>
          <p>- Tenha à sua disposição formulários específicos para cada modelo, que se adaptam às suas necessidades.</p>
          <p>- Obtenha previsões precisas e relevantes para guiar suas decisões de negócios.</p>
        </div>
      </div>
    </div>
  </>
}

export default ServicesSection;
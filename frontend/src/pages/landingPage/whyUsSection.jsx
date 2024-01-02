function WhyUsSection(props) {
  return <>
    <div className='whyus-section'>
      <div className='section-title'>
        <div className='section-divisor'></div>
        <p>Por Que Escolher a Insight ?</p>
      </div>

      <div className='whyus-cards'>
        <div className='whyus-customization whyus-card'>
          <h2>Personalização</h2>
          <p>Acreditamos que os dados são o ativo mais valioso de qualquer empresa e entendemos que cada empresa é única. Portanto, nossos serviços são altamente personalizados para atender às necessidades da sua empresa.</p>
        </div>
        <div className='whyus-expertise whyus-card'>
          <h2>Expertise Técnica</h2>
          <p>Nossa equipe é composta por pessoas criativas, experientes e apaixonadas por análise de dados e Machine Learning e estão compromissadas a garantir os insights que impulsionaram sua empresa ao sucesso.</p>
        </div>
        <div className='whyus-commitment whyus-card'>
          <h2>Excelência</h2>
          <p>Buscamos a excelência em tudo o que fazemos. Nossos serviços são projetados para fornecer insights precisos e confiáveis que impulsionam a tomada de decisões estratégicas.</p>
        </div>
      </div>

      <div>
        <p className='whyus-compromise'>Nos comprometemos a desbloquear o verdadeiro potencial da sua empresa!</p>
        <p className='whyus-compromise'><span>Crie sua conta</span> e junte-se a nós nessa jornada de descoberta e transformação!</p>
      </div>
    </div>
  </>
}

export default WhyUsSection;
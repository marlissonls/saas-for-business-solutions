import TopBar from '../../components/topBar';
import SideBar from '../../components/sideBar';
import MainContent from '../../containers/mainContent';

const mlModelCards = [
  { id: 'A', name: 'Modelo Estatístico', description: 'Em linguística, a noção de texto é ampla e ainda aberta a uma definição mais precisa. Grosso modo, pode ser entendido como manifestação linguística das ideias de um autor, que serão interpretadas pelo leitor de acordo com seus conhecimentos linguísticos e culturais. Seu tamanho é variável.' },
  { id: 'B', name: 'Modelo Medicina', description: 'O interesse pelo texto como objeto de estudo gerou vários trabalhos importantes de teóricos da Linguística Textual, que percorreram fases diversas cujas características principais eram transpor os limites da frase descontextualizada da gramática tradicional e ainda incluir os relevantes papéis do autor e do leitor na construção de textos.' },
  { id: 'C', name: 'Modelo de Vendas', description: 'Vendas' },
  { id: 'A', name: 'Modelo Estatístico', description: 'Estatistico' },
  { id: 'B', name: 'Modelo Medicina', description: 'Medicina' },
  { id: 'C', name: 'Modelo de Vendas', description: 'Vendas' }
];

function MlModelCards(props) {
  return <div className='body'>
    <TopBar />
    <div className='display-flex'>
      <SideBar />
      <MainContent>
        <h2 className='page-title'>Modelos de Machine Learning</h2>

      </MainContent>
    </div>
  </div>
}

export default MlModelCards;
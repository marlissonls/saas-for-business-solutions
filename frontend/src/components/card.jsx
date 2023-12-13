import { Link } from "react-router-dom";

function Card({ route, id, title, description }) {
  return <Link to={`/${route}/${id}`} className='card'>
      <div>
        <p className='card-title'>{title}</p>
        <p className='card-description'>{description}</p>
      </div>
    </Link>
  }
  
export default Card;
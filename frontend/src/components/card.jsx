import { Link } from "react-router-dom";

function Card({ id, title, description }) {
  return <Link to={`/dashboards/${id}`} className='card'>
      <div>
        <p className='card-title'>{title}</p>
        <p className='card-description'>{description}</p>
      </div>
    </Link>
  }
  
export default Card;
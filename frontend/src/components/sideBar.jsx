import { useEffect, useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBuilding, faChartColumn, faCogs } from '@fortawesome/free-solid-svg-icons';

function SideBar(props) {
  
  const location = useLocation();

  const [activeLink, setActiveLink] = useState('/home');

  useEffect(() => {
    const cleanedPathname = location.pathname.replace(/\/[a-f0-9-]+$/, '');
    setActiveLink(cleanedPathname);
  }, [location.pathname]);

  const links = [
    { to: '/home', text: 'Sobre Nós', icon: faBuilding },
    { to: '/models', text: 'Modelos', icon: faCogs },
    { to: '/dashboards', text: 'Analytics', icon: faChartColumn },
  ];

  return (
    <div className='sidebar'>
      {links.map((link, index) => (
        <Link
          key={index}
          to={link.to}
          className={`sidebar-link ${activeLink === link.to ? 'active-link' : ''}`}
        >
          <div className='sidebar-icon-box'>
            <FontAwesomeIcon icon={link.icon} size='lg' />
          </div>
          {link.text}
        </Link>
      ))}
    </div>
  );
}

export default SideBar;

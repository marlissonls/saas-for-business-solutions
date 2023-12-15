import React, { useEffect, useState } from 'react';
import { Link, useNavigate, useLocation } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBuilding, faUser, faChartColumn, faCogs, faSignOut } from '@fortawesome/free-solid-svg-icons';

import { get_profile_url, get_username, get_email, logout } from '../services/auth';

function SideBar(props) {
  const navigate = useNavigate();
  const location = useLocation();

  const [profileImage, setProfileImage] = useState('');
  const [userName, setUserName] = useState('');
  const [email, setEmail] = useState('');
  const [activeLink, setActiveLink] = useState('/home');

  useEffect(() => {
    setProfileImage(`http://127.0.0.1:8000${get_profile_url()}`);
    setUserName(get_username());
    setEmail(get_email());
  }, []);

  useEffect(() => {
    const cleanedPathname = location.pathname.replace(/\/[a-f0-9-]+$/, '');
    setActiveLink(cleanedPathname);
  }, [location.pathname]);

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  const links = [
    { to: '/home', text: 'Empresa', icon: faBuilding },
    { to: '/dashboards', text: 'Dashboards', icon: faChartColumn },
    { to: '/models', text: 'Modelos', icon: faCogs },
    { to: '/profile', text: 'Perfil', icon: faUser },
  ];

  return (
    <div className='sidebar'>
      <div className='profile-container-sidebar'>
        <div className='profile-name-sidebar'>
          <p>{`Olá, ${userName.split(' ')[0]}`}</p>
          <p>{email}</p>
        </div>
        <div className='photo-container-sidebar'>
          <img src={profileImage} className='profile-photo-sidebar' alt='Profile' />
        </div>
      </div>
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
      <div className='sidebar-link logout' onClick={handleLogout}>
        <div className='sidebar-icon-box'>
          <FontAwesomeIcon icon={faSignOut} size='lg' />
        </div>
        Logout
      </div>
    </div>
  );
}

export default SideBar;

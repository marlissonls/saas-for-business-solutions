import React from 'react';
import { Link, useNavigate } from "react-router-dom";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser, faChartSimple, faCogs, faSignOutAlt } from '@fortawesome/free-solid-svg-icons';

import { logout } from '../services/auth';

function SideBar(props) {
  const navigate = useNavigate();

  return (
    <div className='side-bar'>
      <Link to='/profile' className='side-bar-display'>
      <div className='sidebar-icon-box'><FontAwesomeIcon icon={faUser} size='xl' /></div>
        Perfil
      </Link>
      <Link to='/dashboards' className='side-bar-display'>
      <div className='sidebar-icon-box'><FontAwesomeIcon icon={faChartSimple} size='xl' /></div>
        Dashboards
      </Link>
      <Link to='/models' className='side-bar-display'>
      <div className='sidebar-icon-box'><FontAwesomeIcon icon={faCogs} size='xl' /></div>
        Modelos
      </Link>
      <div className='side-bar-display' onClick={() => {
        logout();
        navigate("/login");
      }}>
        <div className='sidebar-icon-box'><FontAwesomeIcon icon={faSignOutAlt} size='xl' /></div>
        Logout
      </div>
    </div>
  );
}

export default SideBar;

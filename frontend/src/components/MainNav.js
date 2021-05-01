import React from 'react';
import { NavLink } from 'react-router-dom';

const MainNav = () => {
  return (
    <div className="navbar-nav mr-auto">
      <span className="navbar-brand">🎥</span>
      <NavLink to="/" exact className="nav-link" activeClassName="router-link-exact-active">
        Home
      </NavLink>
      <NavLink to="/" exact className="nav-link" activeClassName="router-link-exact-active">
        Actors
      </NavLink>
    </div>
  );
}

export default MainNav;

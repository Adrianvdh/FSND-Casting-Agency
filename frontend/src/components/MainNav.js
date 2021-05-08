import React from 'react';
import { NavLink } from 'react-router-dom';

const MainNav = () => {
  return (
    <div className="navbar-nav mr-auto">
      <NavLink to="/movies/">
      <span className="navbar-brand">🎥</span>
      </NavLink>
      <NavLink to="/movies/" exact className="nav-link" activeClassName="router-link-exact-active">
        Movies
      </NavLink>
      <NavLink to="/actors/" exact className="nav-link" activeClassName="router-link-exact-active">
        Actors
      </NavLink>
    </div>
  );
}

export default MainNav;

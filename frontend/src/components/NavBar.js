import React from "react";
import AuthNav from './auth/AuthNav';
import MainNav from './MainNav';


const NavBar = () => {
  return (
    <div className="nav-container mb-3">
      <nav className="navbar navbar-expand-md navbar-light bg-light">
        <div className="container p-0">
          <div className="navbar-brand logo" />
           <MainNav />
           <AuthNav />
        </div>
      </nav>
    </div>
  );
};

export default NavBar;

import React from 'react';
import { useAuth0 } from '@auth0/auth0-react';

import LoginButton from './LoginButton';
import LogoutButton from './LogoutButton';

const AuthNav = () => {
  const { isAuthenticated } = useAuth0();

  return (
    <div className="navbar-nav ml-auto">
      {isAuthenticated ? <LogoutButton /> : <LoginButton />}
    </div>
  );
};

export default AuthNav;

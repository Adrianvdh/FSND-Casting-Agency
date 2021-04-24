import { Route, Switch } from 'react-router-dom';
import { useAuth0 } from '@auth0/auth0-react';
import ProtectedRoute from './auth/protected-route';
import { Home, Profile } from './views'
import { NavBar, Spinner } from './components';

import './App.css';


function App() {
  const { isLoading } = useAuth0();

  if (isLoading) {
    return <Spinner />;
  }

  return (
    <div id="app" className="d-flex flex-column h-100">
      <NavBar />
      <div className="container flex-grow-1">
        <Switch>
          <Route path="/" exact component={Home} />
          <ProtectedRoute path="/profile" component={Profile} />
        </Switch>
      </div>
    </div>
  );
}

export default App;

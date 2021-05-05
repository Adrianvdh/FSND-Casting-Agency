import { Route } from 'react-router-dom';
import { useAuth0 } from '@auth0/auth0-react';
import ProtectedRoute from './auth/protected-route';
import { Home, Profile, Movies, MovieDetail } from './views'
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
        <Route path="/" exact component={Home} />
        <Route path="/movies" exact component={Movies} />
        <Route path="/movies/:movieId" exact component={MovieDetail} />
        <ProtectedRoute path="/profile" component={Profile} />
      </div>
    </div>
  );
}

export default App;

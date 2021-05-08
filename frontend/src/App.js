import { Redirect } from 'react-router-dom';
import { useAuth0 } from '@auth0/auth0-react';
import ProtectedRoute from './auth/protected-route';
import { Profile, Movies, MovieDetail, Actors, ActorDetail } from './views'
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
        <Redirect path="/" to="/movies" />
        <ProtectedRoute path="/movies" exact component={Movies} />
        <ProtectedRoute path="/movies/:movieId" exact component={MovieDetail} />
        <ProtectedRoute path="/actors" exact component={Actors} />
        <ProtectedRoute path="/actors/:actorId" exact component={ActorDetail} />
        <ProtectedRoute path="/profile" component={Profile} />
      </div>
    </div>
  );
}

export default App;

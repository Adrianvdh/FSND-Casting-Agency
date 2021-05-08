import React, {useEffect, useState} from 'react';
import { useAuth0 } from '@auth0/auth0-react';
import axios from "axios";
import MovieCard from '../components/MovieCard';
import ActorCard from "../components/ActorCard";

const Actors = () => {
  const serverUrl = process.env.REACT_APP_SERVER_URL + '/api/actors';
  const { getAccessTokenSilently } = useAuth0();
  const [actors, setActors] = useState([]);
  const [message, setMessage] = useState('');

  useEffect(() => {
    getAccessTokenSilently()
      .then(token => {
        axios
          .get(serverUrl, {
            headers: {
              Authorization: `Bearer ${token}`,
            }
          })
          .then(res => {
            const actors = res.data;
            setActors(actors);
          })
          .catch(err => console.log(err));
      })
      .catch(error => {
        setMessage(error.message);
      })
  }, []);

  return (
      <>
        <h2 className="mb-5 mt-4">🎥 Who to look for</h2>
        <div className="d-flex flex-wrap">
        {actors.map((actor, index) => (
            <ActorCard key={index} actor={actor} />
        ))}
        </div>
      </>
  );
}

export default Actors;

import React, {useEffect, useState} from 'react';
import { useAuth0 } from '@auth0/auth0-react';
import axios from "axios";
import {useParams} from "react-router-dom";
import {Spinner} from "../components";
import ActorGenderEmoji from "../components/ActorGenderEmoji";
import MovieCard from "../components/MovieCard";

const ActorDetail = () => {
  const { actorId } = useParams();
  const serverUrl = process.env.REACT_APP_SERVER_URL + `/api/actors/${actorId}`;
  const { getAccessTokenSilently } = useAuth0();
  const [isLoading, setIsLoading] = useState(true);
  const [actor, setActor] = useState({
    id: undefined,
    full_name: '',
    description: '',
    date_of_birth: '',
    height: 0,
    gender: '',
    cover_image_url: '',
    movies: []
  });
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
                const actor = res.data;
                setActor(actor);
                setIsLoading(false);
              })
              .catch(err => console.log(err));
        })
        .catch(error => {
          setMessage(error.message);
          setIsLoading(false);
        })
  }, []);

  if (isLoading) {
    return <Spinner />;
  }

  return (
      <>
        {/* Movie Detail */}
        <h2 className="mb-5 mt-4"><ActorGenderEmoji actor={actor} /> {actor.full_name}</h2>
        <div className="d-flex flex-wrap">
          <div className="movie-card card">
            <img className="card-img-top" src={ actor.cover_image_url } alt={actor.full_name} />
          </div>
          <div className="d-inline pl-4">
            <div className="d-flex flex-column">
              <div>
                <p style={{'maxWidth': '600px'}}>{actor.description}</p>
              </div>
              <div className="container p-0">
                <div className="row">
                  <div className="col"><p className="font-weight-bold">Born:</p></div>
                  <div className="col"><p>{ actor.date_of_birth }</p></div>
                </div>
                <div className="row">
                  <div className="col"><p className="font-weight-bold">Height:</p></div>
                  <div className="col"><p>{ actor.height }</p></div>
                </div>
              </div>
            </div>
          </div>
        </div>
        {/* Cast list */}
        <h2 className="mb-5 mt-4">🎭 Cast</h2>
        <div className="d-flex flex-wrap">
          {actor.movies.map((movie, index) => (
              <MovieCard key={index} movie={movie} />
          ))}
        </div>

      </>
  );
}

export default ActorDetail;

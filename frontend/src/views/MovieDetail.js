import React, {useEffect, useState} from 'react';
import { useAuth0 } from '@auth0/auth0-react';
import axios from "axios";
import {useParams} from "react-router-dom";
import ActorCard from "../components/ActorCard";
import {Spinner} from "../components";

const MovieDetail = () => {
  const { movieId } = useParams();
  const serverUrl = process.env.REACT_APP_SERVER_URL + `/api/movies/${movieId}`;
  const { getAccessTokenSilently } = useAuth0();
  const [isLoading, setIsLoading] = useState(true);
  const [movie, setMovie] = useState({
    cast: [],
    cover_image_url: '',
    description: '',
    duration: 0,
    genre: '',
    release_date: '',
    title: '',
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
                const movie = res.data;
                console.log(movie)
                setMovie(movie);
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
        <h2 className="mb-5 mt-4">🎥 {movie.title}</h2>
        <div className="d-flex flex-wrap">
          <div className="movie-card card">
            <img className="card-img-top" src={ movie.cover_image_url } alt={movie.title} />
          </div>
          <div className="d-inline pl-4">
            <div className="d-flex flex-column">
              <div>
                <p style={{'maxWidth': '600px'}}>{movie.description}</p>
              </div>
              <div className="container p-0">
                <div className="row">
                  <div className="col"><p className="font-weight-bold">Initial release:</p></div>
                  <div className="col"><p>{ movie.release_date }</p></div>
                </div>
                <div className="row">
                  <div className="col"><p className="font-weight-bold">Duration:</p></div>
                  <div className="col"><p>{ movie.duration }</p></div>
                </div>
                <div className="row">
                  <div className="col"><p className="font-weight-bold">Genre:</p></div>
                  <div className="col"><p>{ movie.genre }</p></div>
                </div>
              </div>
            </div>
          </div>
        </div>
        {/* Cast list */}
        <h2 className="mb-5 mt-4">🎭 Cast</h2>
        <div className="d-flex flex-wrap">
          {movie.cast.map((actor, index) => (
              <ActorCard key={index} actor={actor} />
          ))}
        </div>

      </>
  );
}

export default MovieDetail;

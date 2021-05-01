import React, {useEffect, useState} from 'react';
import { useAuth0 } from '@auth0/auth0-react';
import axios from "axios";
import Movie from '../components/Movie';

const Movies = () => {
  const serverUrl = process.env.REACT_APP_SERVER_URL + '/api/movies';
  const { getAccessTokenSilently } = useAuth0();
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    axios
      .get(serverUrl)
      .then(res => {
        const movies = res.data;
        console.log(movies)
        setMovies(movies);
      })
      .catch(err => console.log(err));
  }, []);

  return (
      <>
        <h2 className="mb-5 mt-4">🎥 What to watch</h2>
        <div className="d-flex flex-wrap">
        {movies.map((movie, index) => (
            <Movie key={index} movie={movie} />
        ))}
        </div>
      </>
  );
}

export default Movies;

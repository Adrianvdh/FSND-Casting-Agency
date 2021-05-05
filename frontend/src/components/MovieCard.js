import React, { useState } from 'react';
import { Link } from "react-router-dom";
import { Spinner } from "./index";

const MovieCard = ({movie}) => {
  const [isLoading, setIsLoading] = useState(true);
  const imageLoaded = () => {
    setIsLoading(false);
  }

  if (isLoading) {
  }
  return (
    <Link to={ '/movies/' + movie.id }>
      <div className="movie-card card">
        <div style={{ display: isLoading ? 'block' : 'none' }}>
          <Spinner />
        </div>
        <div style={{ display: isLoading ? 'none' : 'block' }}>
          <img className="card-img-top" onLoad={imageLoaded} src={ movie.cover_image_url } alt={movie.title} />
        </div>
        <div className="card-body">
          <p className="card-title small">{ movie.title }</p>
        </div>
      </div>
    </Link>
  );
};

export default MovieCard;

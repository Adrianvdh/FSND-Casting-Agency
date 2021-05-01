import React from 'react';

const Movie = ({movie}) => {
  return (
    <div className="movie-card card">
      <img className="card-img-top" src={ movie.cover_image_url } alt={movie.title} />
        <div className="card-body">
          <p className="card-title small">{ movie.title }</p>
        </div>
    </div>
  );
};

export default Movie;

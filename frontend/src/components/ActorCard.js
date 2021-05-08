import React, {useState} from 'react';
import {Spinner} from "./index";
import {Link} from "react-router-dom";

const ActorCard = ({actor}) => {
  const [isLoading, setIsLoading] = useState(true);
  const imageLoaded = () => {
    setIsLoading(false);
  }

  return (
    <Link to={ '/actors/' + actor.id }>
      <div className="movie-card card">
        <div style={{ display: isLoading ? 'block' : 'none' }}>
          <Spinner />
        </div>
        <div style={{ display: isLoading ? 'none' : 'block' }}>
          <img className="card-img-top" onLoad={imageLoaded} src={ actor.cover_image_url } alt={actor.full_name} />
        </div>
        <div className="card-body">
          <p className="card-title small">{ actor.full_name }</p>
        </div>
      </div>
    </Link>
  );
};

export default ActorCard;

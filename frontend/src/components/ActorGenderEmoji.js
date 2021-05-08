import React from 'react';
import spinner from '../static/spinner.gif';

const ActorGenderEmoji = ({ actor }) => {
  if (actor.gender === 'Male') {
    return <>👨</>;
  } else if (actor.gender === 'Female') {
    return <>👩</>;
  } else {
    return <></>;
  }
};

export default ActorGenderEmoji;

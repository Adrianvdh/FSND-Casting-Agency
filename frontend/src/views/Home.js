import React, { useState } from 'react';
import { useAuth0 } from '@auth0/auth0-react';

import axios from "axios";

const Home = () => {
  const serverUrl = process.env.REACT_APP_SERVER_URL;
  const { getAccessTokenSilently } = useAuth0();
  const [message, setMessage] = useState('');

  const getMessage = async () => {
    axios
        .get(serverUrl)
        .then(res => {
          const respMessage = res.data.message;
          setMessage(respMessage);
        })
        .catch(err => console.log(err));
  }
  const getMessageRequiresAuth = () => {
    getAccessTokenSilently()
      .then(token => {
        axios
            .get(serverUrl + '/get-movies', {
              headers: {
                Authorization: `Bearer ${token}`,
              }
            })
            .then(res => {
              const respMessage = res.data.message;
              setMessage(respMessage);
            })
            .catch(err => console.log(err));
      })
      .catch(error => {
        setMessage(error.message);
      })
  }

  return (
    <>
      <h1>Home</h1>
      {message ? message : 'No Message'}
      <button className="btn btn-primary btn-block"
              onClick={() => getMessage()}>Get Message</button>
      <button className="btn btn-primary btn-block"
              onClick={() => getMessageRequiresAuth()}>Get Message Requiring Auth</button>
    </>
);
}

export default Home;

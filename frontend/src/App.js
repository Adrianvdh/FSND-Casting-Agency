import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    axios
      .get('http://localhost:5000/')
      .then(res => {
        const message = res.data.message;
        setMessage(message);
      })
      .catch(err => console.log(err));
  });

  return (
    <div className="container">
      {message ? message : 'Error'}
    </div>
  );
}

export default App;

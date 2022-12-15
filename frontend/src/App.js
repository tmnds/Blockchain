import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import Joke from './Joke';

function App() {
  const [userQuery, setUserQuery] = useState('');
  
  const updateUserQuery = event => {
    console.log('userQuery', userQuery);

    setUserQuery(event.target.value);
  }

  const searchQuery = () => {
    window.open(`https://google.com/search?q=${userQuery}`);
  }

  const handleKeyPress = event => {
    if (event.key === 'Enter') {
      searchQuery();
    }
  }
  return (
    <div className="App">
      <header className="App-header">
      <input value={userQuery} onChange={updateUserQuery} onKeyUpCapture={handleKeyPress}/>
      <button onClick={searchQuery}>Search</button>
      <div>{userQuery}</div>
        <hr />
        <Joke />
        <img src={logo} className="App-logo" alt="logo" />

        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <p>
          New code from .js
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
       
      
      </header>

    </div>
  );
}

export default App;

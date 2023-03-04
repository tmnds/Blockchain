import React, { useState, useEffect } from 'react';
import logo from '../assets/logo.png'
import { API_BASE_URL } from '../config';
import Blockchain from './Blockchain';


function App() {

  const [walletInfo, setWalletInfo] = useState({});

  useEffect(() => {
    fetch(`${API_BASE_URL}/wallet/info`)
    .then(response => response.json())
    .then(json => setWalletInfo(json));

  }, []);

  const { address, balance } = walletInfo;

  return (
    <div className="App">
      <h3> Welcome to CryptoChain </h3>
      <img className='logo' src={logo} alt='application-logo' />
      <div className="WalletInfo">
        <div>Address: {address}</div>
        <div>Balance: {balance}</div>
      </div>
      <br />
      <Blockchain />
    </div>
  );
}

export default App;

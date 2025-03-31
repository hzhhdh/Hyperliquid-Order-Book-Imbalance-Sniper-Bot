// React Component
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function CEXPrice() {
  const [price, setPrice] = useState(null);
  
  useEffect(() => {
    axios.get('https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT')
      .then(res => setPrice(res.data.price));
  }, []);

  return <div>Binance ETH Price: {price}</div>;
}

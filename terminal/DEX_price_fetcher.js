// Node.js (Express)
const axios = require('axios');
const express = require('express');
const app = express();

app.get('/api/dex-price', async (req, res) => {
  try {
    const response = await axios.post('https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3', {
      query: `{ pools(where: {id: "0x..."}) { token0Price token1Price } }`
    });
    res.json(response.data.data.pools[0]);
  } catch (error) {
    res.status(500).json({ error: 'DEX data fetch failed' });
  }
});

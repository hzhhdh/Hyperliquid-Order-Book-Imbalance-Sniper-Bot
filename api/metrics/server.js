const express = require('express');
const app = express();
const port = process.env.PORT || 3001;

// Dummy data for demonstration purposes.
let metrics = {
  liquidity: 55000,
  volume: 850000,
  marketCap: 52000000,
  logs: [
    { timestamp: new Date().toLocaleTimeString(), message: "Liquidity injection executed." },
    { timestamp: new Date().toLocaleTimeString(), message: "Trade volume preserved." },
    { timestamp: new Date().toLocaleTimeString(), message: "Buyback executed to increase market cap." }
  ]
};

app.get('/api/metrics', (req, res) => {
  // Update dummy liquidity randomly for demonstration.
  metrics.liquidity += Math.floor(Math.random() * 500 - 250);
  res.json(metrics);
});

app.listen(port, () => {
  console.log(`Backend API running on port ${port}`);
});

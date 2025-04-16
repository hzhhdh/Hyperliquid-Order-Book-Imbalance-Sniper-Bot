import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, Tooltip, Legend } from 'recharts';
import './Dashboard.css'; // Assume basic styling is defined here

/**
 * Dashboard component provides real-time visibility into trading operations.
 * It displays metrics for liquidity, trading volume, and market capitalization,
 * and logs system events to build trust and transparency.
 */
const Dashboard = () => {
  const [metrics, setMetrics] = useState({
    liquidity: 0,
    volume: 0,
    marketCap: 0,
    logs: []
  });
  const [chartData, setChartData] = useState([]);

  // Fetch latest metrics from backend API every 5 seconds
  useEffect(() => {
    const fetchMetrics = async () => {
      try {
        const response = await axios.get('/api/metrics');
        setMetrics(response.data);
        // Also update chart data: assume backend sends timestamp and liquidity values.
        setChartData(prevData => [...prevData, { time: new Date().toLocaleTimeString(), liquidity: response.data.liquidity }]);
      } catch (error) {
        console.error("Error fetching metrics:", error);
      }
    };
    // Initial fetch
    fetchMetrics();
    const interval = setInterval(fetchMetrics, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="dashboard-container">
      <h1>Automated Trading Dashboard</h1>
      <div className="metrics">
        <div className="metric">
          <h2>Liquidity</h2>
          <p>{metrics.liquidity.toLocaleString()}</p>
        </div>
        <div className="metric">
          <h2>Trading Volume</h2>
          <p>{metrics.volume.toLocaleString()}</p>
        </div>
        <div className="metric">
          <h2>Market Capitalization</h2>
          <p>{metrics.marketCap.toLocaleString()}</p>
        </div>
      </div>
      <div className="chart">
        <h2>Liquidity Over Time</h2>
        <LineChart width={600} height={300} data={chartData}>
          <XAxis dataKey="time" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="liquidity" stroke="#8884d8" />
        </LineChart>
      </div>
      <div className="logs">
        <h2>System Logs</h2>
        <ul>
          {metrics.logs.map((log, index) => (
            <li key={index}>{log.timestamp} - {log.message}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Dashboard;

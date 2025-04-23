import React from 'react';
import PortfolioChart from '../components/PortfolioChart';
import TradeTerminal from '../components/TradeTerminal';
import YieldAnalyzer from '../components/YieldAnalyzer';

export default function Dashboard() {
  return (
    <div className="dashboard">
      <PortfolioChart />
      <TradeTerminal />
      <YieldAnalyzer />
    </div>
  );
}

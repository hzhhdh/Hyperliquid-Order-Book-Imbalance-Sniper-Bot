import React, { useEffect, useState } from 'react';
import { getYieldOpportunities } from '../services/api';

export default function YieldAnalyzer() {
  const [apys, setApys] = useState<number[]>([]);
  useEffect(() => { getYieldOpportunities().then(setApys); }, []);
  return <ul>{apys.map((a,i) => <li key={i}>{a.toFixed(2)}%</li>)}</ul>;
}

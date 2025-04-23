import React, { useEffect } from 'react';
import { useAppSelector, useAppDispatch } from '../store';
import { fetchPortfolio } from '../store/portfolioSlice';
import { Line } from 'recharts';

export default function PortfolioChart() {
  const dispatch = useAppDispatch();
  const { history } = useAppSelector(state => state.portfolio);

  useEffect(() => { dispatch(fetchPortfolio()); }, [dispatch]);

  return <Line data={history} dataKey="value" />;
}

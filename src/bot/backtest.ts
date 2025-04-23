import { Strategy } from './strategyBuilder';

export async function backtest(strategy: Strategy, data: any[]) {
  // simulate
  return data.map(point => ({ ...point, pnl: Math.random() * 10 }));
}

#!/usr/bin/env node
import yargs from 'yargs';
import { buildStrategy } from '../src/bot/strategyBuilder';
import { backtest } from '../src/bot/backtest';

yargs.command('backtest <name>', 'Run backtest', y => {
  y.positional('name', { type: 'string' });
}, async argv => {
  const strat = buildStrategy(argv.name as string, {});
  const result = await backtest(strat, []);
  console.log(result);
}).help().argv;

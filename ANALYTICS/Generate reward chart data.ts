export function generateChartData(stakes: { [key: string]: number }, rewards: { [key: string]: number }): any {
  return {
    labels: Object.keys(stakes),
    datasets: [{ label: 'Rewards', data: Object.values(rewards), borderColor: 'rgba(75, 192, 192, 1)' }],
  };
}

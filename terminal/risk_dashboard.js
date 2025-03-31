// React + Chart.js
import { Doughnut } from 'react-chartjs-2';

const data = {
  labels: ['ETH', 'Stables', 'ALT'],
  datasets: [{
    data: [40, 30, 30],
    backgroundColor: ['#00FFE0', '#32CD32', '#FF4444']
  }]
};

function RiskChart() {
  return <Doughnut data={data} />;
}

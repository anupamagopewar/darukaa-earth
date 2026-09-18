import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js'

import { Line } from 'react-chartjs-2'

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
)

function AnalyticsChart({ analytics }) {
  const labels = analytics.map((item) =>
    new Date(item.date).toLocaleDateString()
  )

  const mainData = {
    labels,
    datasets: [
      {
        label: 'Carbon Value',
        data: analytics.map((item) => item.carbon_value),
        tension: 0.3,
      },
      {
        label: 'Biodiversity Score',
        data: analytics.map((item) => item.biodiversity_score),
        tension: 0.3,
      },
      {
        label: 'Performance Score',
        data: analytics.map((item) => item.performance_score),
        tension: 0.3,
      },
    ],
  }

  const vegetationData = {
    labels,
    datasets: [
      {
        label: 'Vegetation Index',
        data: analytics.map((item) => item.vegetation_index),
        tension: 0.3,
      },
    ],
  }

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: true,
        position: 'top',
        labels: {
          boxWidth: 20,
          padding: 10,
          font: {
            size: 11,
          },
        },
      },
    },
  }

  return (
    <div>
      <h3>Environmental Metrics</h3>

      <div style={{ height: '300px' }}>
        <Line data={mainData} options={options} />
      </div>

      <h3 style={{ marginTop: '30px' }}>Vegetation Index</h3>

      <div style={{ height: '250px' }}>
        <Line data={vegetationData} options={options} />
      </div>
    </div>
  )
}

export default AnalyticsChart
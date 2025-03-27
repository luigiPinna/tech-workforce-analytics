import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js'
import { Line } from 'react-chartjs-2'
import { ArrowLeftIcon } from '@heroicons/react/24/outline'

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend)

function CompanyDetail({ company, onBack }) {
  const chartData = {
    labels: company.data.map(d => d.year).reverse(),
    datasets: [
      {
        label: 'Employee Count',
        data: company.data.map(d => d.employee_count).reverse(),
        borderColor: 'rgb(59, 130, 246)',
        backgroundColor: 'rgba(59, 130, 246, 0.5)',
        tension: 0.1,
      },
    ],
  }

  const chartOptions = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Employee Growth Over Time',
      },
    },
    scales: {
      y: {
        beginAtZero: true,
        ticks: {
          callback: function(value) {
            return value.toLocaleString()
          }
        }
      },
    },
  }

  // Calculate growth rates
  const growthRates = company.data.slice(0, -1).map((d, i) => {
    const nextYear = company.data[i + 1]
    if (!nextYear?.employee_count || !d.employee_count) return null
    return {
      year: d.year,
      growth: ((d.employee_count - nextYear.employee_count) / nextYear.employee_count) * 100
    }
  }).filter(Boolean)

  const growthChartData = {
    labels: growthRates.map(r => r.year),
    datasets: [
      {
        label: 'Year-over-Year Growth Rate (%)',
        data: growthRates.map(r => r.growth),
        borderColor: 'rgb(16, 185, 129)',
        backgroundColor: 'rgba(16, 185, 129, 0.5)',
        tension: 0.1,
      },
    ],
  }

  const growthChartOptions = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Year-over-Year Growth Rate',
      },
    },
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  }

  const latestData = company.data[0]
  const previousData = company.data[1]
  const growth = previousData?.employee_count
    ? ((latestData.employee_count - previousData.employee_count) / previousData.employee_count) * 100
    : 0

  return (
    <div className="space-y-8">
      <button
        onClick={onBack}
        className="flex items-center text-gray-600 hover:text-gray-800"
      >
        <ArrowLeftIcon className="h-5 w-5 mr-2" />
        Back to Dashboard
      </button>

      <div className="bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-2xl font-bold text-gray-800 mb-2">{company.company}</h2>
        <p className="text-gray-600 mb-6">{company.ticker}</p>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <div>
            <p className="text-sm text-gray-500">Latest Employee Count</p>
            <p className="text-2xl font-semibold text-blue-600">
              {latestData.employee_count?.toLocaleString() || 'N/A'}
            </p>
          </div>
          <div>
            <p className="text-sm text-gray-500">Previous Year</p>
            <p className="text-2xl font-semibold text-gray-700">
              {previousData?.employee_count?.toLocaleString() || 'N/A'}
            </p>
          </div>
          <div>
            <p className="text-sm text-gray-500">Growth Rate</p>
            <p className={`text-2xl font-semibold ${growth >= 0 ? 'text-green-600' : 'text-red-600'}`}>
              {growth.toFixed(1)}%
            </p>
          </div>
        </div>

        <div className="space-y-8">
          <div>
            <Line options={chartOptions} data={chartData} />
          </div>
          <div>
            <Line options={growthChartOptions} data={growthChartData} />
          </div>
        </div>
      </div>
    </div>
  )
}

export default CompanyDetail 
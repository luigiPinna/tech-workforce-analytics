import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js'
import { Line } from 'react-chartjs-2'

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend)

function Dashboard({ data, onCompanySelect }) {
  // Calculate total employees across all companies for the latest year
  const latestYear = "2024"
  const totalEmployees = Object.values(data).reduce((sum, company) => {
    const latestData = company.data.find(d => d.year === latestYear)
    return sum + (latestData?.employee_count || 0)
  }, 0)

  // Calculate growth rates
  const growthRates = Object.entries(data).map(([ticker, company]) => {
    const latestData = company.data.find(d => d.year === latestYear)
    const previousData = company.data.find(d => d.year === "2023")
    const growth = previousData?.employee_count 
      ? ((latestData?.employee_count - previousData.employee_count) / previousData.employee_count) * 100
      : 0
    return { ticker, growth }
  })

  const growthChartData = {
    labels: growthRates.map(r => r.ticker),
    datasets: [
      {
        label: 'Employee Growth Rate (%)',
        data: growthRates.map(r => r.growth),
        borderColor: 'rgb(59, 130, 246)',
        backgroundColor: 'rgba(59, 130, 246, 0.5)',
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
        text: 'Employee Growth Rate by Company (2023-2024)',
      },
    },
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  }

  return (
    <div className="space-y-8">
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold text-gray-700">Total Employees</h3>
          <p className="text-3xl font-bold text-blue-600">{totalEmployees.toLocaleString()}</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold text-gray-700">Companies</h3>
          <p className="text-3xl font-bold text-blue-600">{Object.keys(data).length}</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold text-gray-700">Average Growth Rate</h3>
          <p className="text-3xl font-bold text-blue-600">
            {(growthRates.reduce((sum, r) => sum + r.growth, 0) / growthRates.length).toFixed(1)}%
          </p>
        </div>
      </div>

      <div className="bg-white p-6 rounded-lg shadow-md">
        <Line options={growthChartOptions} data={growthChartData} />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {Object.entries(data).map(([ticker, company]) => {
          const latestData = company.data.find(d => d.year === latestYear)
          return (
            <div
              key={ticker}
              onClick={() => onCompanySelect(ticker)}
              className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow cursor-pointer"
            >
              <h3 className="text-xl font-bold text-gray-800">{company.company}</h3>
              <p className="text-sm text-gray-600">{ticker}</p>
              <div className="mt-4">
                <p className="text-sm text-gray-500">Latest Employee Count</p>
                <p className="text-2xl font-semibold text-blue-600">
                  {latestData?.employee_count?.toLocaleString() || 'N/A'}
                </p>
              </div>
            </div>
          )
        })}
      </div>
    </div>
  )
}

export default Dashboard 
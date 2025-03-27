import { useState } from 'react'
import Dashboard from './components/Dashboard'
import CompanyDetail from './components/CompanyDetail'
import Navbar from './components/Navbar'
import employeeData from '../../output/employee_data.json'

function App() {
  const [data, setData] = useState(employeeData)
  const [selectedCompany, setSelectedCompany] = useState(null)

  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar />
      <main className="container mx-auto px-4 py-8">
        {selectedCompany ? (
          <CompanyDetail 
            company={data[selectedCompany]} 
            onBack={() => setSelectedCompany(null)} 
          />
        ) : (
          <Dashboard 
            data={data} 
            onCompanySelect={setSelectedCompany} 
          />
        )}
      </main>
    </div>
  )
}

export default App

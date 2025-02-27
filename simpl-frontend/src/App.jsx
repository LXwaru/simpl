import { BrowserRouter, Route, Routes } from 'react-router-dom'
import './App.css'
import Nav from './components/Nav'
import Home from './components/Home'
import Login from './components/Login'
import Dashboard from './components/Dashboard'
import CreateAccount from './components/CreateAccount'
import CreateCompany from './components/companies/CreateCompany'
import ListClients from './components/clients/ListClients'
import ListEmployees from './components/employees/ListEmployees'
import DetailEmployee from './components/employees/DetailEmployee'
import CreateEmployee from './components/employees/CreateEmployee'
import UpdateEmployee from './components/employees/UpdateEmployee'
import PayRates from './components/employees/PayRates'
import PayrollReport from './components/reports/PayrollReport'
import SearchSales from './components/sales/SearchSales'
import DetailSale from './components/sales/DetailSale'
import CreateSale from './components/sales/CreateSale'
import SearchAppointments from './components/appointments/SearchAppointments'
import ListServices from './components/services/ListServices'
import CreateAppointment from './components/appointments/CreateAppointment'
import AppointmentProcess from './components/appointments/AppointmentProcess'
import CreateService from './components/services/CreateService'
import DetailService from './components/services/DetailService'
import EditService from './components/services/EditService'
import DetailClient from './components/clients/DetailClient'
import CreateClient from './components/clients/CreateClient'
import UpdateClient from './components/clients/UpdateClient'
import ListReports from './components/reports/ListReports'
import Weather from './components/Weather'

const App = () => {

  return (
    <>
      <nav>
      </nav>
    <BrowserRouter>
      <Nav />
      {/* <Weather /> */}
      <div>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/login' element={<Login />} />
          <Route path='/dashboard' element={<Dashboard />} />
          <Route path='/create-account' element={<CreateAccount />} />
          <Route path='/list-employees' element={<ListEmployees />} /> 
          <Route path='/detail-employee/:id' element={<DetailEmployee />} />
          <Route path='/create-employee' element={<CreateEmployee />} />
          <Route path='/update-employee/:id' element={<UpdateEmployee />} />
          <Route path='/pay-rates/:id' element={<PayRates />} />
          <Route path='/payroll-report' element={<PayrollReport />} />
          <Route path='/search-sales' element={<SearchSales />} /> 
          <Route path='/create-sale' element={<CreateSale />} />
          <Route path='/detail-sale/:id' element={<DetailSale />} />
          <Route path='/search-appointments' element={<SearchAppointments />} /> 
          <Route path='/list-services' element={<ListServices />} /> 
          <Route path='/create-company/:id' element={<CreateCompany />} />
          <Route path='/create-appointment' element={<CreateAppointment />} />
          <Route path='/appointment-process/:id' element={<AppointmentProcess />} />
          <Route path='/create-service' element={<CreateService />} />
          <Route path='/detail-service/:id' element={<DetailService />} />
          <Route path='/edit-service/:id' element={<EditService />} />
          <Route path='/list-clients' element={<ListClients />} /> 
          <Route path='/detail-client/:id' element={<DetailClient />} />
          <Route path='/create-client' element={<CreateClient />} />
          <Route path='/update-client/:id' element={<UpdateClient />} />
          <Route path='/list-reports' element={<ListReports />} />
        </Routes>
      </div>
    </BrowserRouter>
    </>
)
}

export default App

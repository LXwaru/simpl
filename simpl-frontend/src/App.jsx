import { BrowserRouter, Route, Routes } from 'react-router-dom'
import './App.css'
import Nav from './components/Nav'
import Home from './components/Home'
import Login from './components/Login'
import Dashboard from './components/Dashboard'
import CreateAccount from './components/CreateAccount'
import CreateCompany from './components/CreateCompany'
import ListClients from './components/ListClients'
import ListEmployees from './components/ListEmployees'
import ListSales from './components/ListSales'
import ListAppointments from './components/ListAppointments'
import ListServices from './components/services/ListServices'
import CreateAppointment from './components/appointments/CreateAppointment'
import CreateSale from './components/sales/CreateSale'
import CreateService from './components/services/CreateService'
import DetailService from './components/services/DetailService'
import EditService from './components/services/EditService'

const App = () => {

  return (
    <>
      <nav>
      </nav>
    <BrowserRouter>
      <Nav />
      <div>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/login' element={<Login />} />
          <Route path='/dashboard' element={<Dashboard />} />
          <Route path='/create-account' element={<CreateAccount />} />
          <Route path='/list-clients' element={<ListClients />} /> 
          <Route path='/list-employees' element={<ListEmployees />} /> 
          <Route path='/list-sales' element={<ListSales />} /> 
          <Route path='/list-appointments' element={<ListAppointments />} /> 
          <Route path='/list-services' element={<ListServices />} /> 
          <Route path='/create-company' element={<CreateCompany />} />
          <Route path='/create-appointment' element={<CreateAppointment />} />
          <Route path='/create-sale' element={<CreateSale />} />
          <Route path='/create-service' element={<CreateService />} />
          <Route path='/detail-service/:id' element={<DetailService />} />
          <Route path='/edit-service/:id' element={<EditService />} />
        </Routes>
      </div>
    </BrowserRouter>
    </>
)
}

export default App

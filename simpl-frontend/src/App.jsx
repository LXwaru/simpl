import { BrowserRouter, Route, Routes } from 'react-router-dom'
import './App.css'
import Nav from './components/Nav'
import Home from './components/Home'
import Login from './components/Login'
import Dashboard from './components/Dashboard'
import CreateAccount from './components/CreateAccount'
import CompanyDetails from './components/CompanyDetails'
import ListClients from './components/ListClients'
import ListEmployees from './components/ListEmployees'
import ListSales from './components/ListSales'
import ListAppointments from './components/ListAppointments'
import ListServices from './components/ListServices'

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
          <Route path='/companydetails' element={<CompanyDetails />} />
          <Route path='/listclients' element={<ListClients />} /> 
          <Route path='/listemployees' element={<ListEmployees />} /> 
          <Route path='/listsales' element={<ListSales />} /> 
          <Route path='/listappointments' element={<ListAppointments />} /> 
          <Route path='/listservices' element={<ListServices />} /> 
        </Routes>
      </div>
    </BrowserRouter>
    </>
)
}

export default App

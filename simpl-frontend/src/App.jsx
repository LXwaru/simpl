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
          <Route path='/list-clients' element={<ListClients />} /> 
          <Route path='/list-employees' element={<ListEmployees />} /> 
          <Route path='/list-sales' element={<ListSales />} /> 
          <Route path='/list-appointments' element={<ListAppointments />} /> 
          <Route path='/list-services' element={<ListServices />} /> 
          <Route path='/create-company' element={<CreateCompany />} />
        </Routes>
      </div>
    </BrowserRouter>
    </>
)
}

export default App

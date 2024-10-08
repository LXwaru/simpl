import { BrowserRouter, Route, Routes } from 'react-router-dom'
import './App.css'
import Nav from './components/Nav'
import Home from './components/Home'
import Login from './components/Login'
import Dashboard from './components/Dashboard'
import CreateAccount from './components/CreateAccount'

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
        </Routes>
      </div>
    </BrowserRouter>
    </>
)
}

export default App

import { BrowserRouter, Route, Routes } from 'react-router-dom'
import './App.css'
import Nav from './components/Nav'
import Home from './components/Home'
import Login from './components/Login'
import Dashboard from './components/Dashboard'

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
        </Routes>
      </div>
    </BrowserRouter>
    </>
)
}

export default App

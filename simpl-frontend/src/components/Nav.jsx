import { useEffect, useState } from 'react'
import { NavLink } from 'react-router-dom'
import axios from 'axios'



const Nav = () => {
    const [ token, setToken ] = useState('access-token')
    const [ username, setUsername ] = useState('')


    useEffect(() => {
        const fetchToken= async () => {
            const accessToken = localStorage.getItem('access_token')
            console.log(accessToken)
            setToken(accessToken)
            const tokenResponse = await axios.get('http://localhost:8000/token', {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            })
            console.log(tokenResponse)
            
        }
        fetchToken()
    }, [token])

    // useEffect(() => {
    //     const fetchUser = async () => {
    //         const userResponse = 
    //     }
    // }, [])


    return (
        <>
            <nav className="navbar bg-body-tertiary fixed-top">
            <div className="container-fluid">
                <NavLink className="navbar-brand" to="/">simpl business solutions [s | b | s ]</NavLink>

                <NavLink className="navbar-brand" to="/login">login or create account</NavLink>
                <button className="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
                </button>
                <div className="offcanvas offcanvas-end" tabIndex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
                <div className="offcanvas-header">
                    <h5 className="offcanvas-title" id="offcanvasNavbarLabel">S|B|S - welcome</h5>
                    <button type="button" className="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
                </div>
                <div className="offcanvas-body">
                    <ul className="navbar-nav justify-content-end flex-grow-1 pe-3">
                    <li className="nav-item">
                        <a className="nav-link active" aria-current="page" href="/">home</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="/login">login or create account</a>
                    </li>
                    </ul>
                </div>
                </div>
            </div>
            </nav>
        </>
    )
}
export default Nav
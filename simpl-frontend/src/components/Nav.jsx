import { useEffect, useState } from 'react'
import { NavLink, useNavigate } from 'react-router-dom'
import axios from 'axios'



const Nav = () => {
    const [ username, setUsername ] = useState('')
    const navigate = useNavigate()
    const accessToken = localStorage.getItem('access_token')


    useEffect(() => {
        const token = localStorage.getItem('access_token')
        const fetchAdminData = async () => {
            const adminResponse = await axios.get('http://localhost:8000/users/me', {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            })
            // console.log(adminResponse.data.username)
            setUsername(adminResponse.data.username)
        }
        fetchAdminData()
    }, [username])

        const handleLogout = () => {
            localStorage.removeItem('access_token')
            navigate('/')
            
        }

    return (
        <>
            <nav className="navbar bg-body-tertiary fixed-top">
            <div className="container-fluid">
                <NavLink className="navbar-brand" to="/">simpl business solutions [s | b | s ]</NavLink>
                {accessToken && (
                    <button className='navbar-brand' onClick={handleLogout}>logout</button>
                )}
                {!accessToken && (
                    <NavLink className="navbar-brand" to="/login">login or create account</NavLink>

                )}
                <button className="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
                </button>
                <div className="offcanvas offcanvas-end" tabIndex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
                <div className="offcanvas-header">
                    <h5 className="offcanvas-title" id="offcanvasNavbarLabel">[s | b | s] - welcome {username}</h5>
                    <button type="button" className="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
                </div>
                <div className="offcanvas-body">
                    <ul className="navbar-nav justify-content-end flex-grow-1 pe-3">
                        <li className="nav-item">
                            <a className="nav-link active" aria-current="page" href="/dashboard">dashboard</a>
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
import { NavLink, useNavigate } from 'react-router-dom'
import axios from 'axios'
import { useSelector, useDispatch } from 'react-redux'
import { logout } from '../features/user/userSlice'



const Nav = () => {
    // const [ user, setUser ] = useState(null)
    // const [ isAuthenticated, setIsAuthenticated ] = useState(false)
    const user = useSelector((state) => state.user.value)
    const navigate = useNavigate()
    const dispatch = useDispatch()

    const handleLogout = async () => {
        try {
            await axios.post('http://localhost:8000/api/logout', {}, {
                withCredentials: true
            })
            dispatch(logout())
            console.log('logout successful')
            navigate('/')
        } catch (error) {
            console.error('logout failed', error)
        }
    }

    return (
        <>
            <nav className="navbar bg-body-tertiary fixed-top">
            <div className="container-fluid">
                <NavLink className="navbar-brand" to="/">simpl business solutions [ s | b | s ]</NavLink>
                    {user ? (
                        <>
                            {user?.company?.name ? (
                                <NavLink className='navbar-brand' to='/dashboard'>{user.company.name} </NavLink>
                            ) : (
                                <NavLink className='navbar-brand' to={`/create-company/${user.id}`}>register new company</NavLink>
                            )}
                            <NavLink className='navbar-brand' onClick={handleLogout}>logout</NavLink>
                        </>
                    ) : (
                        <NavLink className='navbar-brand' to='/login'>login or create account</NavLink>
                    )}
                <button className="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
                </button>
                <div className="offcanvas offcanvas-end" tabIndex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
                <div className="offcanvas-header">
                    <h5 className="offcanvas-title" id="offcanvasNavbarLabel">[ s | b | s ] - welcome {user?.username || 'guest'}</h5>
                    <button type="button" className="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
                </div>
                <div className="offcanvas-body">
                    <ul className="navbar-nav justify-content-end flex-grow-1 pe-3">
                        {user ? (
                            <>
                                <li className="nav-item">
                                    <NavLink className="nav-link active" aria-current="page" to="/dashboard">dashboard</NavLink>
                                </li>
                                <li className="nav-item">
                                    <NavLink className="nav-link active" aria-current="page" to="/list-services">services</NavLink>
                                </li>
                                <li className="nav-item">
                                    <NavLink className="nav-link active" aria-current="page" to="/list-clients">clients</NavLink>
                                </li>
                                <li className="nav-item">
                                    <NavLink className="nav-link active" aria-current="page" to="/list-employees">employees</NavLink>
                                </li>
                                <li className="nav-item">
                                    <NavLink className="nav-link active" aria-current="page" to="/create-sale">register a sale</NavLink>
                                </li>
                                <li className="nav-item">
                                    <NavLink className="nav-link active" aria-current="page" to="/create-appointment">make an appointment</NavLink>
                                </li>
                                <li className="nav-item">
                                    <NavLink className="nav-link active" aria-current="page" to="/list-reports">reports</NavLink>
                                </li>
                            </>
                        ):(
                            <p>please log in</p>
                        )}
                    </ul>
                </div>
                </div>
            </div>
            </nav>
        </>
    )
}
export default Nav
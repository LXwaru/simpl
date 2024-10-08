import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'

const Login = () => {
    const [ username, setUsername ] = useState('')
    const [ password, setPassword ] = useState('')
    const [ token, setToken ] = useState('')
    const navigate = useNavigate()

    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            const { data: loginResponse } = await axios.post(
                'http://localhost:8000/token', 
                new URLSearchParams({
                    grant_type: 'password',
                    username: username,
                    password: password,
                    scope: '',
                    client_id: '',
                    client_secret: ''
            }),
            {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            }
        )
        localStorage.setItem('access_token', loginResponse.access_token)
        setToken(loginResponse.access_token)
        console.log('login successful, token saved', loginResponse.access_token)
        // window.location.reload()
        navigate('/dashboard')
        } catch (error) {
            console.error('login failed', error)
        }
    }

    // useEffect(() => {
    //     const fetchAdminData = async () => {
    //         const response = await axios.get('http://localhost:8000/users/me', {
    //             headers: {
    //                 Authorization: `Bearer ${token}`
    //             }
    //         })
    //         console.log(response)
    //     }
    //     fetchAdminData()
    // }, [token])

    const handleUsernameChange = (e) => {
        e.preventDefault()
        setUsername(e.target.value)
    }

    const handlePasswordChange = (e) => {
        e.preventDefault()
        setPassword(e.target.value)
    }

    return (
        <>
            <div className="container-sm">
                <form 
                    className='form-control'
                    onSubmit={handleSubmit}
                >
                    <label>
                        <h3>
                            login
                        </h3>
                    </label>
                    <input 
                        type="username" 
                        onChange={handleUsernameChange}
                        className="form-control" 
                        id="username" 
                        placeholder="username" />
                    <input 
                        type="password" 
                        onChange={handlePasswordChange}
                        className="form-control" 
                        id="password" 
                        placeholder="password" />
                    <button 
                        type="submit" 
                        className='btn btn-success'>
                            submit
                    </button>
                    <br />
                </form>
                    <button 
                        type="link" 
                        className='btn btn-link'>
                            create account
                    </button>
            </div>
        </>
    )
}
export default Login
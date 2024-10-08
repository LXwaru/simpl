import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'

const Login = () => {
    const [ username, setUsername ] = useState('')
    const [ password, setPassword ] = useState('')
    const navigate = useNavigate()

    // useEffect (() => {
    //     try {
    //         const loginResponse = axios.post('http://localhost:8000/token', {
    //             username: username,
    //             password: password
    //         },
    //         {
    //             headers: {
    //                 'Content-Type': 'application/json'
    //             }
    //         }
    //     )
    //         console.log(loginResponse.data)

    //     } catch (error) {
    //     }
    // }, [username, password])

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
        console.log('login successful, token saved', loginResponse.access_token)
        // navigate('/dashboard')
        } catch (error) {
            console.error('login failed', error)
        }
    }

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
                    <button 
                        type="link" 
                        className='btn btn-link'>
                            create account
                    </button>
                </form>
            </div>
        </>
    )
}
export default Login
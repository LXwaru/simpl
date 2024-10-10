import { useState, useEffect } from 'react'
import { useNavigate, Link } from 'react-router-dom'
import axios from 'axios'
import { useDispatch } from 'react-redux'
import { setUser } from '../features/user/userSlice'

const Login = () => {
    const [ username, setUsername ] = useState('')
    const [ password, setPassword ] = useState('')
    const [ errorMessage, setErrorMessage ] = useState('')
    const navigate = useNavigate()
    const dispatch = useDispatch()

    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            const { data: loginResponse } = await axios.post(
                'http://localhost:8000/token', 
                new URLSearchParams({
                    grant_type: 'password',
                    username: username,
                    password: password,
            }),
            {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                withCredentials: true
            }
        )
        const userResponse = await axios.get('http://localhost:8000/users/me', {
            withCredentials: true
        })

        dispatch(setUser(userResponse.data))

        setErrorMessage('')

        console.log('login successful, token saved', loginResponse)
        navigate('/dashboard')
        } catch (error) {
            console.error('login failed', error)
            setErrorMessage('login failed. check credentials and try again')
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
                        {errorMessage && <p className='text-danger'>{errorMessage}</p>}
                    </label>
                    <input 
                        type="username" 
                        onChange={handleUsernameChange}
                        value={username}
                        className="form-control" 
                        id="username" 
                        placeholder="username"
                        required
                    />
                    <input 
                        type="password" 
                        onChange={handlePasswordChange}
                        value={password}
                        className="form-control" 
                        id="password" 
                        placeholder="password" 
                        required
                    />
                    <button 
                        type="submit" 
                        className='btn btn-success'>
                            submit
                    </button>
                    <br />
                </form>
                    <Link
                        className='btn btn-link' 
                        to='/create-account'>create account
                    </Link>
            </div>
        </>
    )
}
export default Login
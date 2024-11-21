import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import { useDispatch } from 'react-redux'
import { setUser } from '../features/user/userSlice'


const CreateAccount = () => {
    const [ username, setUsername ] = useState('')
    const [ password, setPassword ] = useState('')
    const [ confirmPassword, setConfirmPassword ] = useState('')
    const [ errorMessage, setErrorMessage ] = useState('')
    const navigate = useNavigate()
    const dispatch = useDispatch()
    


    const handleSubmit = async () => {
        if (password !== confirmPassword) {
            alert('passwords do not match')
            return
        }
        try {
            const payload = {
                'username': username,
                'password': password,
            }
            axios.post('http://localhost:8000/api/admins/', payload)
            alert('admin creation successful')
            navigate('/login')
            
        } catch (error) {
            console.error('could not register new admin', error)
        } finally {
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
    }



    const handleNameChange = (e) => {
        e.preventDefault()
        console.log(e.target.value)
        setUsername(e.target.value)
    }

    const handlePasswordChange = (e) => {
        e.preventDefault()
        console.log(e.target.value)
        setPassword(e.target.value)
    }

    const handleConfirmPasswordChange = (e) => {
        e.preventDefault()
        console.log(e.target.value)
        setConfirmPassword(e.target.value)
    }

    return (
        <>
            <form 
                    className='form-control'
                    onSubmit={handleSubmit}
                >
                <label>register new admin</label>
                <input 
                        type="username" 
                        onChange={handleNameChange}
                        className="form-control" 
                        id="username" 
                        placeholder="username" />
                <input 
                        type="password" 
                        onChange={handlePasswordChange}
                        className="form-control" 
                        id="password" 
                        placeholder="password" />
                <input 
                        type="password" 
                        onChange={handleConfirmPasswordChange}
                        className="form-control" 
                        id="confirm-password" 
                        placeholder="confirm password" />
                <button className='btn btn-success'>submit</button>
            </form>
        </>
    )
}
export default CreateAccount
import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'


const CreateAccount = () => {
    const [ username, setUsername ] = useState('')
    const [ password, setPassword ] = useState('')
    const [ confirmPassword, setConfirmPassword ] = useState('')
    const navigate = useNavigate()
    


    const handleSubmit = () => {
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
            
        } catch (error) {
            console.error('could not register new admin', error)
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
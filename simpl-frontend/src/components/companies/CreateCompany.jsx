import { Link, useNavigate } from 'react-router-dom'
import { useState, useEffect } from 'react'
import axios from 'axios'
import { useSelector, useDispatch } from 'react-redux'
import {  updateUser } from '../../features/user/userSlice'


const CreateCompany = () => {
    const user = useSelector((state) => state.user.value)
    const [ companyName, setCompanyName ] = useState('')
    const [ companyDescription, setCompanyDescription ] = useState('')
    const dispatch = useDispatch()
    const navigate = useNavigate()


    const handleCompanyNameChange = (e) => {setCompanyName(e.target.value)}
    const handleDescriptionChange = (e) => {setCompanyDescription(e.target.value)}

    const handleSubmit = async (e) => {
        e.preventDefault()
        if (!companyName || !companyDescription) {
            alert('please provide a company name AND company description')
            return 
        }
        try {
            const payload = {
                name: companyName,
                description: companyDescription
            }
            await axios.post(`http://localhost:8000/api/companies/${user.id}`, payload, {
                withCredentials: true
            })
            alert('company successfully registered')
            navigate('/dashboard')
            const { data: updatedUser } = await axios.get(`http://localhost:8000/users/me`, {
                withCredentials: true
            })

            dispatch(updateUser(updatedUser))

        } catch (error) {
            console.error('could not register company', error)
        }
    }

    return(

        <>
        <div className='form-control'>
            <form onSubmit={handleSubmit}>
                <h3>register a new company</h3>
                <div className='form-floating mb-3'>
                    <input onChange={handleCompanyNameChange} type='text' className='form-control' id='company-title' placeholder='title' />
                    <label htmlFor='company-name'>company title</label>
                </div>
                <div className='form-floating mb-3'>
                    <input onChange={handleDescriptionChange} type='text' className='form-control' id='company-description' placeholder='description' />
                    <label htmlFor='company-description'>description</label>
                </div>
                <button className='btn btn-light'type='submit'>submit</button>
            </form>
        </div>
        </>
    )
}
export default CreateCompany
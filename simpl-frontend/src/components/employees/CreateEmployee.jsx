import { useSelector, useDispatch } from 'react-redux'
import { useState, useEffect } from 'react'
import { useNavigate, Link } from 'react-router-dom'
import axios from 'axios'
import { updateUser } from '../../features/user/userSlice'

const CreateEmployee = () => {
    const company_id = useSelector((state) => state.user.value.company.id)
    const navigate = useNavigate()
    const dispatch = useDispatch()
    const [ name, setName ] = useState('')
    const [ email, setEmail ] = useState('')

    const handleNameChange = (e) => {setName(e.target.value)}
    const handleEmailChange = (e) => {setEmail(e.target.value)}

    const handleSubmit = async (e) => {
        e.preventDefault()
        if (!name || !email) {
            alert('you must enter a name and an email')
            return
        }
        try{
            const payload = {
                full_name: name,
                email: email
            }
            await axios.post(`http://localhost:8000/api/employees/${company_id}/`, payload, {
                withCredentials: true
            })
            alert('employee successfully registered')
            navigate('/list-employees')

            const { data: updatedUser } = await axios.get(`http://localhost:8000/users/me`, {
                withCredentials: true
            })

            dispatch(updateUser(updatedUser))
        } catch (error) {
            console.error('could not create employee', error)
        }
    }
    return(
        <>
            <div className='form-control'>
                <h3>register a new employee</h3>
                <form onSubmit={handleSubmit}>
                <div className="form-floating mb-3">
                        {/* full_name */}
                        <input onChange={handleNameChange} type="text" className="form-control" id="name" placeholder="name" />
                        <label htmlFor="name">full name</label>
                    </div>
                    <div className="form-floating mb-3">
                        <input onChange={handleEmailChange} type="email" className="form-control" id="email" placeholder="email" />
                        <label htmlFor="email">email</label>
                    </div>
                    <button className='btn btn-primary'>submit</button>
                </form>
                <Link to='/list-employees'>employee list</Link>
            </div>
        </>
    )
}
export default CreateEmployee
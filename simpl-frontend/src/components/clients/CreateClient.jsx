import { Link, useNavigate } from 'react-router-dom'
import { useState, useEffect } from 'react'
import axios from 'axios'
import { useSelector, useDispatch } from 'react-redux'
import { setUser, updateUser } from '../../features/user/userSlice'


const CreateClient = () => {

    const company_id = useSelector((state) => state.user.value.company.id) 
    const navigate = useNavigate()
    const dispatch = useDispatch()
    const [ name, setName ] = useState('')
    const [ email, setEmail ] = useState('')
    const handleNameChange = (e) => {setName(e.target.value)}
    const handleEmailChange = (e) => {setEmail(e.target.value)}


    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            const payload = {
                full_name: name,
                email: email
            }

            await axios.post(`http://localhost:8000/api/clients/${company_id}/`, payload, {
                withCredentials: true
            })
            alert('client successfully registered')
            navigate('/list-clients')
            const { data: updatedUser } = await axios.get(`http://localhost:8000/users/me`, {
                withCredentials: true
            })

            dispatch(updateUser(updatedUser))

        } catch (error) {
            console.error('could not register new client', error)
        }
    }

    return (
        <>
            <div className='container-fluid form-control'>
                <form onSubmit={handleSubmit}>
                    <h3>register a new client</h3>
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
                <Link to='/list-client'>client list</Link>
            </div>
        </>
    )
}
export default CreateClient
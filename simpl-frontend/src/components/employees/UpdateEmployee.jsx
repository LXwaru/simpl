import { Link, useNavigate, useParams } from 'react-router-dom'
import { useState, useEffect } from 'react'
import axios from 'axios'
import { useSelector, useDispatch } from 'react-redux'
import { setUser, updateUser } from '../../features/user/userSlice'


const UpdateEmployee = () => {
    const {id} = useParams()
    const dispatch = useDispatch()
    const user = useSelector((state) => state.user.value)
    const company_id = user.company.id
    const employees = user.company.employees
    const employee = employees.find((employee) => employee.id === parseInt(id, 10))
    const [ name, setName ] = useState(employee.full_name)
    const [ email, setEmail ] = useState(employee.email)



    const handleNameChange = (e) => {setName(e.target.value)}
    const handleEmailChange = (e) => {setEmail(e.target.value)}

    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            const payload = {
                full_name: name,
                email: email
            }
            await axios.put(`http://localhost:8000/api/employee_info/${company_id}/${id}`, payload, {
                withCredentials: true
            })

            const { data: updatedUser } = await axios.get(`http://localhost:8000/users/me`, {
                withCredentials: true
            })

            dispatch(updateUser(updatedUser))

        } catch (error) {
            console.error('could not edit employee', error)
        }
    } 
    return (
        <>
            <div className='form-control'>
                <h3>edit employee information: </h3><br />
                <p>
                    name: {employee.full_name} <br />
                    email: {employee.email} 
                </p>
                <hr />   
                <form onSubmit={handleSubmit}>
                    <div className='form-floating mb-3'>
                        <input onChange={handleNameChange} type='text' className='form-control' id='name' placeholder={'name'}/>
                        <label htmlFor='name'>edit name</label>
                    </div>
                    <div className='form-floating mb-3'>
                        <input onChange={handleEmailChange} type='email' className='form-control' id='email' placeholder={'email'}/>
                        <label htmlFor='email'>edit email</label>
                    </div>
                    <button type='submit' className='btn btn-light'>submit</button>
                </form>
            <Link to={`/detail-employee/${id}`}>back to {employee.full_name}'s details</Link>

            </div>
        </>
    )
}
export default UpdateEmployee
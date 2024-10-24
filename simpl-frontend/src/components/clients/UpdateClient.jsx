import { Link, useNavigate, useParams } from 'react-router-dom'
import { useState, useEffect } from 'react'
import axios from 'axios'
import { useSelector, useDispatch } from 'react-redux'
import { setUser, updateUser } from '../../features/user/userSlice'


const UpdateClient = () => {
    const {id} = useParams()
    const navigate = useNavigate()
    const dispatch = useDispatch()
    const user = useSelector((state) => state.user.value)
    const company_id = user.company.id
    const clients = user.company.clients
    if (!clients) {
        return <div>Loading clients...</div>
    }
    const client = clients.find((client) => client.id === parseInt(id, 10))
    const [ name, setName ] = useState(client.full_name)
    const [ email, setEmail ] = useState(client.email)

    const handleNameChange = (e) => {setName(e.target.value)}
    const handleEmailChange = (e) => {setEmail(e.target.value)}

    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            const payload = {
                full_name: name,
                email: email
            }
            await axios.put(`http://localhost:8000/api/client/${company_id}/${id}/`, payload, {
                withCredentials: true
            })
            alert('client successfully updated')
            navigate(`/detail-client/${id}`)

            const { data: updatedUser } = await axios.get(`http://localhost:8000/users/me`, {
                withCredentials: true
            })

            dispatch(updateUser(updatedUser))
        } catch (error) {
            console.error('could not update client', error)
        }
    }

    return (
        <>
            <div className='container-fluid form-control'>
                <form onSubmit={handleSubmit}>
                <h3>edit client information: {client.full_name}</h3>
                    <div className="form-floating mb-3">
                        <input onChange={handleNameChange} type="text" className="form-control" id="name" placeholder={"name"} />
                        <label htmlFor="name">full name</label>
                    </div>
                    <div className="form-floating mb-3">
                        <input onChange={handleEmailChange} type="email" className="form-control" id="email" placeholder={"email"} />
                        <label htmlFor="email">email address</label>
                    </div>
                    <button className='btn btn-light'>submit</button>
                </form>
            </div>
        </>
    )
}
export default UpdateClient
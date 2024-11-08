import axios from 'axios'
import { useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { updateUser } from '../../features/user/userSlice'
import { useNavigate, Link } from 'react-router-dom'

const CreateSale = () => {
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const user = useSelector((state) => state.user.value)
    const companyId = user.company.id
    const clients = user.company.clients
    const services = user.company.services 
    const [ clientId, setClientId ] = useState(0)
    const [ serviceIds, setServiceIds ] = useState([])
    
    
    const handleClientChange = (e) => setClientId(e.target.value)
    const addToServiceList = (id) => {
        setServiceIds((prevServiceIds) => [...prevServiceIds, id])
        console.log([...serviceIds, id])
    }
    const clearServiceIds = () => {
        setServiceIds([])
    }


    const handleSubmit = async (e) => {
        e.preventDefault()
        if (!clientId || serviceIds.length === 0) {
            alert('select client AND services')
            return
        }
        try {

            const payload = {
                client_id: clientId,
                service_ids: serviceIds
            }
            axios.post(`http://localhost:8000/api/${companyId}/sales/`, payload, {
                withCredentials: true
            })
            alert('sale successfully registered')
            navigate('/list-sales')
            const { data: updatedUser } = await axios.get(`http://localhost:8000/users/me`, {
                withCredentials: true
            })
            dispatch(updateUser(updatedUser))

        } catch (error) {
            console.error('could not register sale', error)
        }
    }

    return (
        <>
            <div className='form-control'>
                <form onSubmit={handleSubmit}>
                    <h3>register a sale</h3>
                    <select
                        onChange={handleClientChange}
                        className="form-select form-select-sm" 
                        aria-label="Small select example"
                        defaultValue=''>
                            <option value='' disabled>select an client</option>
                        {clients.map((client) => (
                            <option key={client.id} value={client.id}>{client.full_name}</option>
                        ))}
                    </select>
                    <table className='table'>
                        <thead>
                            <tr>
                                <th>service list</th>
                            </tr>
                        </thead>
                        <tbody>
                            {services.map((service) => (
                                <tr key={service.id}>
                                    <td>{service.title}</td>
                                    <td><button type='button' className='btn btn-light' onClick={() => addToServiceList(service.id)}>add to sale</button></td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                    <h5>
                        selected services <br />
                        <button 
                        type='button'
                        className='btn btn-link'
                        onClick={clearServiceIds}>clear selected services</button>
                    </h5>
                        {serviceIds.map((serviceId) => (
                    <ul className='list-group' key={serviceId}>
                        <li className='list-group-item'>{serviceId}</li>
                    </ul>
                        ))}
                    <button 
                    type='submit'
                    className='btn btn-primary'
                    >submit</button>
                </form>
            </div>
        </>
    )
}
export default CreateSale
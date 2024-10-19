import { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import axios from 'axios'
import { useSelector, useDispatch } from 'react-redux'
import { setUser, updateUser } from '../../features/user/userSlice'
import { Link, useNavigate } from 'react-router-dom'


const DetailService = () => {

    const {id} = useParams()
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const user = useSelector((state) => state.user.value)
    const company_id = useSelector((state) => state.user.value.company.id)    
    const services = useSelector((state) => state.user.value.company.services)
    
    if (!services) {
        return <div>Loading services...</div>
    }
    const service = services.find((service) => service.id === parseInt(id, 10))

    const deactivateService = async () => {
        try {
            await axios.put(`http://localhost:8000/api/${company_id}/service_activation_toggle/${id}`, {}, {
                withCredentials: true
            })
            alert('service deactivated')

            const { data: updatedUser } = await axios.get(`http://localhost:8000/users/me`, {
                withCredentials: true
            })
            dispatch(updateUser(updatedUser))
            navigate('/list-services')
        } catch (error) {
            console.error('could not deactivate service', error)
        }
    }

    const deleteService = async () => {
        try {
            await axios.delete(`http://localhost:8000/api/${company_id}/service/${id}`, {
                withCredentials: true
            })
            alert('service deleted')
            const { data: updatedUser } = await axios.get(`http://localhost:8000/users/me`, {
                withCredentials: true
            })
            dispatch(updateUser(updatedUser))
            navigate('/list-services')
        } catch (error) {
            console.error('could not delete service', error)
        }
    }


    return (
        <>
            <div className='form-control container-fluid'>
                <h3>{service.title} - ${service.price}
                    
                </h3>
                    
                <p>{service.description}</p>
                <ul>
                    <li>
                        <Link className='btn btn-light' to='/create-sale'>purchase</Link>
                    </li>
                    <li>
                        <Link className='btn btn-light' to='/create-appointment'>reserve</Link> 
                    </li>
                    <li>
                        <Link className='btn btn-light' to={`/edit-service/${service.id}`}>edit service details</Link>
                    </li>
                    <li>
                        <button className='btn btn-light' onClick={() => deactivateService(service.id)}>deactivate service</button>
                    </li>
                    <li>
                        <Link className='btn btn-danger' onClick={deleteService}>delete this service</Link>
                    </li>
                </ul>

                


            </div>
            <Link to='/list-services'>return to service list</Link>
        </>
    )
}
export default DetailService
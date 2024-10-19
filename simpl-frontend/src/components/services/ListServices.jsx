import { useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { setUser, updateUser } from '../../features/user/userSlice'
import { Link } from 'react-router-dom'
import axios from 'axios'



const ListServices = () => {

    const user = useSelector((state) => state.user.value)
    const company_id = useSelector((state) => state.user.value.company.id)    
    const services = user.company.services
    const activeServices = services.filter(service => service.is_enabled === true)
    const disabledServices = services.filter(service => service.is_enabled === false)
    const dispatch = useDispatch()
    const reactivateService = async (service_id) => {
        try {
            await axios.put(`http://localhost:8000/api/${company_id}/service_activation_toggle/${service_id}`, {}, {
                withCredentials: true
            })
            alert('service reactivated')

            const { data: updatedUser } = await axios.get(`http://localhost:8000/users/me`, {
                withCredentials: true
            })
            dispatch(updateUser(updatedUser))
        } catch (error) {
            console.error('could not reactivate service', error)
        }
    }

    const formatDuration = (isoDuration) => {
        // Use a regular expression to capture hours, minutes, and seconds
        const regex = /P(T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?)?/;
        const matches = isoDuration.match(regex);
        
        if (!matches) {
            return "Invalid duration format";
        }
    
        const hours = matches[2] ? parseInt(matches[2], 10) : 0;
        const minutes = matches[3] ? parseInt(matches[3], 10) : 0;
        const seconds = matches[4] ? parseInt(matches[4], 10) : 0;
        
        let result = '';
        
        if (hours) {
            result += `${hours} hour${hours > 1 ? 's' : ''} `
        }
        if (minutes) {
            result += `${minutes} minute${minutes > 1 ? 's' : ''} `;
        }
        if (seconds) {
            result += `${seconds} second${seconds > 1 ? 's' : ''}`;
        }
            
        return result.trim();
    }

    return (
        <>
            <div className='container-fluid form-control'>
                <h3>Services</h3>
                <Link to='/create-service'>register a new service</Link>
                <table className='table'>
                    <thead>
                        <tr>
                            <td>title</td>
                            <td>price</td>
                            <td>duration</td>
                        </tr>
                    </thead>
                    <tbody>
                        {activeServices.map((service) => (
                        <tr key={service.id}>
                            <td>
                                <Link to={`/detail-service/${service.id}`}>{service.title}</Link>
                            </td>
                            <td>${service.price} USD</td>
                            <td>{formatDuration(service.duration)}</td>
                        </tr>
                        ))}
                    </tbody>
                </table>
            </div>
            <div className="accordion" id="accordionExample">
                <div className="accordion-item">
                    <h2 className="accordion-header">
                    <button className="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                        disabled services
                    </button>
                    </h2>
                    <div id="collapseOne" className="accordion-collapse collapse show" data-bs-parent="#accordionExample">
                        <div className="accordion-body">                           
                        {disabledServices.map((service) =>(
                            <ul className='list-group' key={service.id}>
                                <li className='list-group-item'>
                                    {service.title}<button className='btn btn-link' onClick={() => reactivateService(service.id)}>reactivate service</button>
                                </li>
                            </ul>
                        ))}
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}
export default ListServices
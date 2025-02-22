import { useSelector, useDispatch } from 'react-redux'
import { useEffect, useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import axios from 'axios'
import { Link } from 'react-router-dom'
import { updateUser } from '../../features/user/userSlice'

const AppointmentProcess = () => {
    const [loading, setLoading] = useState(false)
    const [creditId, setCreditId] = useState(0)
    const { id } = useParams()
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const user = useSelector((state) => state.user.value)
    const companyId = user.company.id
    const appointments = user.company.appointments
    const services = user.company.services
    const clients = user.company.clients
    const employees = user.company.employees
    const appointment = appointments.find((appointment) => appointment.id === parseInt(id, 10))
    const service = services.find((service) => service.id === appointment.service_id)
    const client = clients.find((client) => client.id === appointment.client_id)
    const employee = employees.find((employee) => employee.id === appointment.employee_id)


    const formatDateTime = (dateTime) => {
        const date = new Date(dateTime)
        const daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
        const dayOfWeek = daysOfWeek[date.getDay()];
        const month = (date.getMonth() + 1).toString().padStart(2, '0')
        const day = date.getDate().toString().padStart(2, '0')
        const year = date.getFullYear()
        let hours = date.getHours()
        const minutes = date.getMinutes().toString().padStart(2, '0')
        const ampm = hours >= 12 ? 'pm' : 'am'
        hours = hours % 12 || 12
        const formattedDate = `${month}/${day}/${year}`
        const formattedTime = `${hours}:${minutes}${ampm}`
        return `${dayOfWeek}, ${formattedDate} at ${formattedTime}`
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
    
    const handleCreditIdChange = (e) => {
        setCreditId(e.target.value)
    }

    const applyCredit = async (id) => {
        try {
            setLoading(true)
            await axios.put(`http://localhost:8000/api/${companyId}/apply_credit/${id}/${creditId}`, {
                withCredentials: true
            })
            const { data: updatedUser } = await axios.get(`http://localhost:8000/users/me`, {
                withCredentials: true
            })

            dispatch(updateUser(updatedUser))
        } catch (error) {
            console.error('an error occurred when applying credit', error)
        } finally {
            setLoading(false)
        }
    }

    const removeCredit = async (id) => {
        try {
            await axios.put(`http://localhost:8000/api/${companyId}/remove_credit/${id}/${creditId}`, {
                withCredentials: true
            })
            alert('credit removed from appointment')
            const { data: updatedUser } = await axios.get(`http://localhost:8000/users/me`, {
                withCredentials: true
            })
            dispatch(updateUser(updatedUser))
        } catch (error) {
            console.error('could not remove credit', error)
        }
    }

    const confirmAppointment = (isConfirmed, id) => {
        if (!isConfirmed) {
            const confirm = async (id) => {
                try {
                    await axios.put(`http://localhost:8000/api/${companyId}/appointment_confirm/${id}`, {
                        withCredentials: true
                    })
                    const { data: updatedUser } = await axios.get(`http://localhost:8000/users/me`, {
                        withCredentials: true
                    })
                    dispatch(updateUser(updatedUser))
                } catch (error) {
                    console.error("could not confirm appointment", error)
                }
            }
            return <button className="btn btn-link" onClick={() => confirm(id)}>confirm</button>
        } else {
            return "confirmed"
        }
    }
    const getCredits = (clientId, serviceId) => {
        try {
            const clients = user.company.clients
            const services = user.company.services
            const service = services.find((service) => service.id === parseInt(serviceId, 10))
            const client = clients.find((client) => client.id === parseInt(clientId, 10))
            const credits = client.credits
            const filteredCredits = credits.filter((credit) => credit.service_id === parseInt(serviceId, 10))
            const unredeemedCredits = filteredCredits.filter((credit) => credit.is_redeemed === false)
            const availableCredits = unredeemedCredits.filter((credit) => credit.is_attached === false)
            return (
                <>
                    {!availableCredits.length? (
                        <div>
                            <p><i>no credits available</i></p>
                            <Link 
                                className='btn btn-secondary btn-sm'
                                to='/create-sale'>
                                register sale
                            </Link>
                        </div>
                    ) : (
                        <div>
                            <select
                                onChange={handleCreditIdChange}
                                className='form-select'
                                aria-label='select'
                                defaultValue={0}
                            >
                                <option value={0}>select credit</option>
                                {availableCredits.map((credit) => (
                                <option key={credit.id} value={credit.id}>{credit.service_title}, sale id {credit.sale_id}</option>
                                ))}
                            </select>
                            <button 
                                className='btn btn-success' 
                                onClick={() => applyCredit(id)}>
                                apply credit to appointment
                            </button>
                        </div>
                    )}
                </>
                
            )
        } catch (error) {
            console.error('something is messed up', error)
        }
    }

    const checkoutAppointment = async (id)=> {
        
        try {
            await axios.put(`http://localhost:8000/api/${companyId}/appointment_checkout/${id}/`, {
                withCredentials: true
            })
            alert('appointment successfully checked out')
            navigate('/dashboard')
            const { data: updatedUser } = await axios.get(`http://localhost:8000/users/me`, {
                withCredentials: true
            })

            dispatch(updateUser(updatedUser))
        } catch (error) {
            console.error('could not checkout appointment', error)
        }
    }
    

    const cancelAppointment = async (id) => {
        try{
            await removeCredit(id)
            await axios.put(`http://localhost:8000/api/${companyId}/appointment_cancel/${id}/`, {
                withCredentials: true
            })
            alert('appointment successfully cancelled')
            const { data: updatedUser } = await axios.get(`http://localhost:8000/users/me`, {
                withCredentials: true
            })

            dispatch(updateUser(updatedUser))
            navigate('/dashboard')
        } catch (error) {
            console.error('could not cancel appointment', error)
            if (error.response.status === 401) {
                alert('you must remove the credit from the appointment before cancelling')
            }
        }
    }

    if (loading) {
        return <div><p>Loading...</p></div>
    }
    return (
        <>
            <div className='form-control'>
                <h3>{employee.full_name}: {service.title} with {employee.full_name}</h3>
                <table className='table'>
                    <thead>
                        <tr>
                        <th>date/time</th>
                        <th>duration</th>
                        <th>confirm</th>
                        <th>checkout</th>
                        <th>cancel appointment</th>
                        </tr>
                    </thead>
                    <tbody>
                        {appointment.is_complete ? (
                        <tr>
                            <td>{formatDateTime(appointment.start_time)}</td>
                            <td>{formatDuration(service.duration)}</td>
                            <td>complete</td>
                            <td>checked out</td>
                            <td>
                                <button className='btn btn-danger disabled' onClick={() => cancelAppointment(id)}>appointment has already been completed</button>
                            </td>
                        </tr>
                            ) : (  
                        <tr>
                            <td>{formatDateTime(appointment.start_time)}</td>
                            <td>{formatDuration(service.duration)}</td>
                            <td>{confirmAppointment(appointment.is_confirmed, appointment.id)}</td>
                            {appointment.credit ? (
                                <td>
                                <button className='btn btn-primary' onClick={() => checkoutAppointment(appointment.id)}>
                                checkout appointment
                                </button>
                                <button className='btn btn-link' onClick={() => removeCredit(appointment.id)}>remove credit</button>
                                </td>       
                            ) : (
                                <td>{getCredits(appointment.client_id, appointment.service_id, appointment.id)}</td>
                            )}
                            {appointment.credit ? (
                                <td>
                                <button className='btn btn-danger disabled'>remove credit to cancel
                                </button>
                                </td>
                            ) : (
                                <td>
                                    <button className='btn btn-danger' onClick={() => cancelAppointment(id)}>cancel appointment</button>
                                </td>
                            )}
                        </tr>
                        )}
                    </tbody>
                </table>
            </div>
        </>
    )
}

export default AppointmentProcess
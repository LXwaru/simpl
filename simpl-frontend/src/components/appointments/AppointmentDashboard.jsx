import { useEffect, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import axios from 'axios'
import { useSelector, useDispatch } from 'react-redux'
import { updateUser } from '../../features/user/userSlice'


const AppointmentDashboard = () => {
    const user = useSelector((state) => state.user.value)
    const companyId = user.company.id
    const appointments = user.company.appointments
    const [ creditId, setCreditId ] = useState(0)
    const [ loading, setLoading ] = useState(false)
    const dispatch = useDispatch()


    const getEmployeeName = (employeeId) => {
        const employees = user.company.employees
        const employee = employees.find((employee) => employee.id === parseInt(employeeId, 10))
        return employee.full_name
    }


    const getClientName = (clientId) => {
        const clients = user.company.clients
        const client = clients.find((client) => client.id === parseInt(clientId, 10))
        return client.full_name
    }


    const getServiceTitle = (serviceId) => {
        const services = user.company.services
        const service = services.find((service) => service.id === parseInt(serviceId, 10))
        return service.title
    }


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


    const handleCreditIdChange = (e) => {
        setCreditId(e.target.value)
    }


    const getCredits = (clientId, serviceId, appointmentId) => {
        try {
            const clients = user.company.clients
            const services = user.company.services
            const service = services.find((service) => service.id === parseInt(serviceId, 10))
            const client = clients.find((client) => client.id === parseInt(clientId, 10))
            const credits = client.credits
            const filteredCredits = credits.filter((credit) => credit.service_id === parseInt(serviceId, 10))
            const availableCredits = filteredCredits.filter((credit) => credit.is_redeemed === false)
            return (
                <>
                    {!availableCredits? (
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
                                onClick={() => applyCredit(appointmentId)}>
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


    const applyCredit = async (appointmentId) => {
        try {
            setLoading(true)
            await axios.put(`http://localhost:8000/api/${companyId}/apply_credit/${appointmentId}/${creditId}`, {
                withCredentials: true
            })
            const { data: updatedUser } = await axios.get(`http://localhost:8000/users/me`, {
                withCredentials: true
            })

            dispatch(updateUser(updatedUser))
        } catch (error) {
            console.error('an error occurred when applying credit')
        } finally {
            setLoading(false)
        }
    }
    
    const cancelAppointment = async (appointmentId) => {
        try{
            await axios.delete(`http://localhost:8000/api/${companyId}/appointment/${appointmentId}/`, {
                withCredentials: true
            })
            alert('appointment successfully cancelled')
            const { data: updatedUser } = await axios.get(`http://localhost:8000/users/me`, {
                withCredentials: true
            })

            dispatch(updateUser(updatedUser))
        } catch (error) {
            console.error('could not cancel appointment', error)
        }
    }

    if (loading) {
        return <div><p>Loading...</p></div>
    }

    return (
        <>
            {appointments? (
            <div className='form-control'>
                <h3>upcoming appointments</h3>
                    <table className='table'>
                        <thead>
                            <tr>
                                <th>client</th>
                                <th>service</th>
                                <th>employee</th>
                                <th>date/time</th>
                                <th>checkout</th>
                                <th>cancel appointment</th>
                            </tr>
                        </thead>
                        <tbody>
                        {appointments.map(appointment => (
                            <tr key={appointment.id}>
                                <td>{getClientName(appointment.client_id)}</td>
                                <td>{getServiceTitle(appointment.service_id)}</td>
                                <td>{getEmployeeName(appointment.employee_id)}</td>
                                <td>{formatDateTime(appointment.start_time)}</td>
                                {appointment.credit? (
                                    <td>
                                            <button className='btn btn-primary' onClick={() => checkoutAppointment(appointment.id)}>
                                                checkout appointment
                                            </button>
                                    </td>
                                ) : (
                                    <td>{getCredits(appointment.client_id, appointment.service_id, appointment.id)}</td>
                                )}
                                <td>
                                    <button className='btn btn-link' onClick={() => cancelAppointment(appointment.id)}>cancel appointment</button>
                                </td>
                            </tr>
                        ))}
                        </tbody>
                    </table>
            </div>
            ) : (
                <div>
                    <h3>no appointments</h3>
                </div>
            )}
        </>
    )
}
export default AppointmentDashboard
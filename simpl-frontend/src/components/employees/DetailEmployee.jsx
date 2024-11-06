import Calendar from '../Calender'
import { useParams } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'
import { updateUser } from '../../features/user/userSlice'
import { Link, useNavigate } from 'react-router-dom'
import axios from 'axios'

const DetailEmployee = () => {
    const {id} = useParams()
    const user = useSelector((state) => state.user.value)
    const companyId = user.company.id
    const employees = user.company.employees
    const employee = employees.find((employee) => employee.id === parseInt(id, 10))
    const rightNow = new Date()
    const appointments = employee.appointments
    const upcomingAppointments = appointments.filter((appointment) => 
        new Date(appointment.start_time) > rightNow)
    const pastAppointments = appointments.filter((appointment) => 
        new Date(appointment.start_time) < rightNow) 
    const clients = user.company.clients
    const services = user.company.services
    const dispatch = useDispatch()

    const getClientName = (clientId) => {
        const client = clients.find((client) => client.id === clientId)
        return client.full_name
    }

    const getServiceName = (serviceId) => {
        const service = services.find((service) => service.id === serviceId)
        return service.title
    }

    const formatDateTime = (dateTime) => {
        const date = new Date(dateTime)

        const daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
        const dayOfWeek = daysOfWeek[date.getDay()];

        // in short date format
        const month = (date.getMonth() + 1).toString().padStart(2, '0')
        const day = date.getDate().toString().padStart(2, '0')
        const year = date.getFullYear()


        let hours = date.getHours()
        const minutes = date.getMinutes().toString().padStart(2, '0')
        const ampm = hours >= 12 ? 'pm' : 'am'

        hours = hours % 12 || 12

        // for short date format
        const formattedDate = `${month}/${day}/${year}`
        const formattedTime = `${hours}:${minutes}${ampm}`
        return `${dayOfWeek}, ${formattedDate} at ${formattedTime}`
    }

    const checkoutStatus = (checkedOutStatus) => {
        if (checkedOutStatus) {
            return <strong>checked out</strong>
        } else {
            return <em>not checked out</em>
        }
    }

    const confirmAppointment = async (eventId) => {
        try {
            await axios.put(`http://localhost:8000/api/${companyId}/appointment_confirm/${eventId}`, {
                withCredentials: true
            })
            const { data: updatedUser } = await axios.get(`http://localhost:8000/users/me`, {
                withCredentials: true
            })

            dispatch(updateUser(updatedUser))
        } catch (error) {
            console.error('could not confirm appointment', error)
        }
    }
    
    const deleteAppointment = async (eventId) => {
        try {
            await axios.delete(`http://localhost:8000/api/${companyId}/appointment/${eventId}`, {
                withCredentials: true
            })
            alert('successfully deleted appointment')
            const { data: updatedUser } = await axios.get(`http://localhost:8000/users/me`, {
                withCredentials: true
            })

            dispatch(updateUser(updatedUser))
        } catch (error) {
            console.error('could not delete appointment', error)
        }
    } 

    return(
        <>
            <div className='form-control'>
            <h3>{employee.full_name}</h3>
            <Link to={`/update-employee/${id}`}>update employee information</Link>
                <h3>upcoming appointments</h3>
                <table className='table'>
                    <thead>
                        <tr>
                            <th>date/time</th>
                            <th>service</th>
                            <th>client</th>
                            <th>confirm</th>
                            <th>cancel appointment</th>
                        </tr>
                    </thead>
                    <tbody>
                {upcomingAppointments
                .sort((a, b) => new Date(a.start_time) - new Date(b.start_time))
                .map((appointment) => (
                    <tr key={appointment.id}>
                        <td>{formatDateTime(appointment.start_time)}</td>
                        <td>{getServiceName(appointment.service_id)}</td>
                        <td>{getClientName(appointment.client_id)}</td>
                        {appointment.is_confirmed ? (
                            <>
                            <td>
                            <Link onClick={()=>confirmAppointment(appointment.id)} >unconfirm</Link>
                            </td>
                            </>
                        ) : (
                        <td>
                            <Link onClick={()=>confirmAppointment(appointment.id)} >confirm</Link>
                        </td>
                        )}
                        <td>
                            <Link onClick={()=>deleteAppointment(appointment.id)} >cancel</Link>
                        </td>
                    </tr>
                ))}
                        
                    </tbody>
                </table>
                <div className="accordion" id="appointment">
                    <div className="accordion-item">
                            <h2 className="accordion-header">
                            <button className="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#past_appointment" aria-expanded="false" aria-controls="past_appointment">
                                past appointments: 
                            </button>
                            </h2>
                            <div id="past_appointment" className="accordion-collapse collapse" data-bs-parent="#past_appointment">
                                <table className='table'>
                                    <thead>
                                        <tr>
                                            <th>date/time</th>
                                            <th>service</th>
                                            <th>client</th>
                                            <th>status</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                {pastAppointments.map((appointment) => (
                                    <tr key={appointment.id}>
                                        <td>{formatDateTime(appointment.start_time)}</td>
                                        <td>{getServiceName(appointment.service_id)}</td>
                                        <td>{getClientName(appointment.client_id)}</td>
                                        <td>{checkoutStatus(appointment.is_complete)}</td>
                                    </tr>
                                ))}
                                        
                                    </tbody>
                                </table>
                            </div>
                        </div>
                </div>
            </div>
        </>
    )
}
export default DetailEmployee
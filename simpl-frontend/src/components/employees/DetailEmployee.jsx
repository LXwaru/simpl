import Calendar from '../Calender'
import { useParams } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'
import { Link, useNavigate } from 'react-router-dom'

const DetailEmployee = () => {
    const {id} = useParams()
    const user = useSelector((state) => state.user.value)
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
    
    return(
        <>
            <h3>{employee.full_name}</h3>
            <Link to={`/update-employee/${id}`}>manage schedule</Link>
            <div className='form-control'>
                <h3>upcoming appointments</h3>
                <table className='table'>
                    <thead>
                        <tr>
                            <th>date/time</th>
                            <th>service</th>
                            <th>client</th>
                        </tr>
                    </thead>
                    <tbody>
                {upcomingAppointments.map((appointment) => (
                    <tr key={appointment.id}>
                        <td>{formatDateTime(appointment.start_time)}</td>
                        <td>{getServiceName(appointment.service_id)}</td>
                        <td>{getClientName(appointment.client_id)}</td>
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
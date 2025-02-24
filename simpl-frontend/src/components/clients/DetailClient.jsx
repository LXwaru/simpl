import { useParams } from 'react-router-dom'
import { useState } from 'react'
import axios from 'axios'
import { useSelector, useDispatch } from 'react-redux'
import { updateUser } from '../../features/user/userSlice'
import { Link, useNavigate } from 'react-router-dom'



const DetailClient = () => {

    const {id} = useParams()
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const user = useSelector((state) => state.user.value)
    const sales = user.company.sales
    const company_id = user.company.id
    const clients = user.company.clients
    const services = user.company.services
    const client = clients.find((client) => client.id === parseInt(id, 10))
    const clientSales = client.sales
    const credits = client.credits
    const employees = user.company.employees
    const rightNow = new Date()
    const activeCredits = credits.filter((credit) => credit.is_redeemed === false)
    const redeemedCredits = credits.filter((credit) => credit.is_redeemed === true)
    const appointments = client.appointments
    const upcomingAppointments = appointments.filter((appointment) => {
        const appointmentStartTime = new Date(appointment.start_time)
        return appointmentStartTime > rightNow
    })    
    const pastAppointments = appointments.filter((appointment) => {
        const appointmentStartTime = new Date(appointment.start_time)
        return appointmentStartTime < rightNow
    })
    const pastOrFuture = (startTime) => {
        const appointmentStartTime = new Date(startTime)
        if (appointmentStartTime < rightNow) {
            return 'past'
        } else {
            return 'upcoming'
        }
    }
    const isCompleteStatus = (completeStatus) => {
        if (completeStatus === true) {
            return "complete"
        } else {
            return 'incomplete'
        }
    }
    const getServiceName = (serviceId) => {
        const service = services.find((service) => service.id === serviceId)
        return service.title
    }
    const getEmployeeName = (employeeId) => {
        const employee = employees.find((employee) => employee.id === employeeId)
        return employee.full_name
    }
    // for appointments
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
    // for sale data
    const getSaleDate = (saleId) => {
        const sale = sales.find((sale) => sale.id === saleId)
        if (sale && sale.date) {
            const saleDate = new Date(sale.date)
            return saleDate.toLocaleString()
        } else {
            return 'date not available'
        }
    }
    const formatDuration = (serviceId) => {
        const service = services.find((service) => service.id === serviceId)
        const duration = service.duration
        // Use a regular expression to capture hours, minutes, and seconds
        const regex = /P(T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?)?/;
        const matches = duration.match(regex);
        
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
    const isRedeemed = (isRedeemed) => {
        if (isRedeemed) {
            return 'redeemed'
        } else {
            return 'active'
        }
    }

    const cancelAppointment = async(id) => {
        try {
            axios.put(`http://localhost:8000/api/${company_id}/appointment_cancel/${id}/`, {
                withCredentials: true
            })
            const { data: updatedUser } = await axios.get(`http://localhost:8000/users/me`, {
                withCredentials: true
            })
            dispatch(updateUser(updatedUser))
            
        } catch (error) {
            console.error('could not cancel appointment', error)
        }
        
    }

    return (
        <>
            <div className='container-fluid form-control'>
                <div className='form-control'>

                    <hr /><h3>{client.full_name}</h3><hr />
                    <h6>
                    <strong>client email: </strong><Link to={`mailto:${client.email}`}>{client.email}</Link><br />
                    <hr />
                    <Link to={`/update-client/${id}`}>update client information
                    </Link>
                    </h6>
                </div>
                <div className="accordion" id="credits">
                    <div className="accordion-item">
                        <h2 className="accordion-header">
                        <button className="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#activeCredits" aria-expanded="true" aria-controls="activeCredits">
                            credits:
                        </button>
                        </h2>
                        <div id="activeCredits" className="accordion-collapse collapse" data-bs-parent="#credits">
                            <div className="accordion-body">
                                <h5 className='form-control'><strong><hr />
                                total credits: {credits.length} <hr /> </strong>
                                active credits: {activeCredits.length} <br /> 
                                redeemed credits: {redeemedCredits.length} <hr /></h5>
                                <table className='table'>
                                    <thead>
                                        <tr>
                                            <td>service</td>
                                            <td>active/redeemed</td>
                                            <td>purchased on:</td>
                                            <td>sale id</td>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {credits.map((credit) => (
                                            <tr key={credit.id}>
                                                <td>{credit.service_title}</td>
                                                <td>{isRedeemed(credit.is_redeemed)}</td>
                                                <td>{getSaleDate(credit.sale_id)}</td>
                                                <td>{credit.sale_id}</td>
                                            </tr>
                                        )).reverse()}
                                    </tbody>
                                </table>               
                            </div>
                        </div>
                    </div>
                    <div className="accordion-item">
                        <h2 className="accordion-header">
                        <button className="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseFour" aria-expanded="false" aria-controls="collapseFour">
                            appointments: 
                        </button>
                        </h2>
                        <div id="collapseFour" className="accordion-collapse collapse" data-bs-parent="#credits">
                            <div className="accordion-body">
                                <h5 className='form-control'><hr /><strong>current date/time:</strong> {formatDateTime(new Date())}
                                <hr />
                                <strong>total appointments: </strong>{appointments.length} <br />
                                upcoming appointments: {upcomingAppointments.length}<br />
                                past appointments: {pastAppointments.length}
                                <hr />
                                </h5>
                                <table className='table'>
                                    <thead>
                                        <tr>
                                            <td>service</td>
                                            <td>employee</td>
                                            <td>date/time</td>
                                            <td>duration</td>
                                            <td>checked out status</td>
                                            <td>force cancel appointment</td>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {appointments.map((appointment) => (
                                            appointment.is_cancelled ? (
                                                <tr key={appointment.id} className='disabled'>
                                                    <td>{getServiceName(appointment.service_id)}</td>
                                                    <td>{getEmployeeName(appointment.employee_id)}</td>
                                                    <td>{formatDateTime(appointment.start_time)}</td>
                                                    <td>{formatDuration(appointment.service_id)}</td>
                                                    <td>{isCompleteStatus(appointment.is_complete)}</td>
                                                    <td>appointment cancelled</td>
                                                </tr>
                                            ) : (
                                            appointment.is_complete ? (
                                            <tr key={appointment.id}>                               
                                                <td>{getServiceName(appointment.service_id)}</td>
                                                <td>{getEmployeeName(appointment.employee_id)}</td>
                                                <td>{formatDateTime(appointment.start_time)}</td>
                                                <td>{formatDuration(appointment.service_id)}</td>
                                                <td>{isCompleteStatus(appointment.is_complete)}</td>
                                                <td>
                                                    <button className='btn btn-danger' onClick={() => cancelAppointment(appointment.id)}>cancel appointment</button>
                                                </td>
                                            </tr>
                                            ) : (
                                            <tr key={appointment.id}>
                                                <td>{getServiceName(appointment.service_id)}</td>
                                                <td>{getEmployeeName(appointment.employee_id)}</td>
                                                <td>{formatDateTime(appointment.start_time)}</td>
                                                <td>{formatDuration(appointment.service_id)}</td>
                                                <td>{isCompleteStatus(appointment.is_complete)}</td>
                                                <td>n/a</td>
                                            </tr>
                                            )
                                        ))).reverse()}
                                    </tbody>
                                </table>                           
                            </div>
                        </div>
                    </div>
                    <div className="accordion-item">
                        <h2 className="accordion-header">
                        <button className="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseFive" aria-expanded="false" aria-controls="collapseFive">
                            sales history:
                        </button>
                        </h2>
                        <div id="collapseFive" className="accordion-collapse collapse" data-bs-parent="#credits">
                            <div className="accordion-body">
                                <h5 className='form-control'><hr />total sales: {clientSales.length}<hr /></h5>
                                <table className='table'>
                                    <thead>
                                        <tr>
                                            <td>sale ID</td>
                                            <td>date/time</td>
                                            <td>services</td>
                                            <td>total</td>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {clientSales.map((sale) => (
                                        <tr key={sale.id}>
                                            <td>{sale.id}</td>
                                            <td>{getSaleDate(sale.id)}</td>
                                            <td>
                                            {sale.credits.map((credit) => (
                                                <ul className='list-group' key={credit.id}>
                                                    <li className='list-group-item'>{getServiceName(credit.service_id)}</li>
                                                </ul>
                                            ))}
                                            </td>
                                            <td>${sale.total_due} USD</td>
                                        </tr>
                                        ))}
                                    </tbody>
                                </table>                           
                            </div>
                        </div>
                    </div>
                </div>
                <Link to='/list-clients'>back to client list</Link>
            </div>
        </>
    )
}
export default DetailClient
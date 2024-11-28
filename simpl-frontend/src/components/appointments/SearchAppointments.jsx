import { Link } from 'react-router-dom'
import { useSelector } from 'react-redux'
import { useState, useEffect } from 'react'

const SearchAppointments
 = () => {
    const [ clientValue, setClientValue ] = useState('')
    const [ serviceValue, setServiceValue ] = useState('')
    const [ employeeValue, setEmployeeValue ] = useState('')
    const [ dateValue, setDateValue ] = useState('')
    const user = useSelector((state) => state.user.value)
    const clients = user.company.clients
    const services = user.company.services
    const employees = user.company.employees 
    const todayDateTime = new Date()
    const appointments = user.company.appointments
    const [ whichAppointments, setWhichAppointments ] = useState([])


    const formattedDateTime = (dateTime) => {
        const date = new Date(dateTime)

        const daysOfWeek = ['Sun', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat'];
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
        return `${formattedDate} - ${formattedTime}`
    }

    const showAllAppointments = () => {setWhichAppointments(appointments)}

    const showUpcomingAppointments = () => {
        const rightNow = new Date()
        const upcoming = appointments.filter((appointment) => new Date(appointment.start_time )> rightNow)
        setWhichAppointments(upcoming)
    }
    const showPastAppointments = () => {
        const rightNow = new Date()
        const past = appointments.filter((appointment) => new Date(appointment.start_time) < rightNow)
        setWhichAppointments(past)
    }


    const getClientName = (id) => {
        const client = clients.find(client => client.id === id)
        return client.full_name
    }
    const getServiceName = (id) => {
        const service = services.find(service => service.id === id)
        return service.title
    }
    const getEmployeeName = (id) => {
        const employee = employees.find(employee => employee.id === id)
        return employee.full_name
    }
    const confirmStatus = (status) => {
        if (status) {
            return 'confirmed'
        } else {
            return 'unconfirmed'
        }
    }
    const checkoutStatus = (status) => {
        if (status) {
            return 'complete'
        } else {
            return <strong>incomplete</strong>
        }
    }
    const paymentStatus = (status) => {
        if (status) {
            return 'paid'
        } else {
            return <strong>need payment</strong>
        }
    }
    
    
    const clientFilter = whichAppointments.filter((appointment) => getClientName(appointment.client_id).toLowerCase().includes(clientValue.toLowerCase()))
    const serviceFilter = clientFilter.filter((appointment) => getServiceName(appointment.service_id).toLowerCase().includes(serviceValue.toLowerCase()))
    const employeeFilter = serviceFilter.filter((appointment) => getEmployeeName(appointment.employee_id).toLowerCase().includes(employeeValue.toLowerCase()))
    const dateFilter = employeeFilter.filter((appointment) => {
        const formattedDate = formattedDateTime(appointment.start_time).toLowerCase()
        return formattedDate.includes(dateValue)
    })
    
    const handleClientFilterChange = (e) => {setClientValue(e.target.value)}
    const handleServiceFilterChange = (e) => {setServiceValue(e.target.value)}
    const handleEmployeeFilterChange = (e) => {setEmployeeValue(e.target.value)}
    const handleDateFilterChange = (e) => {setDateValue(e.target.value)}

    
    return (
        <>
            <div className='form-control'>
                <h3>appointment search</h3>
                <p>{formattedDateTime(todayDateTime)}</p>
                <h5>
                <button type='button' className='btn btn-link' onClick={showAllAppointments}>
                    all appointments
                    </button>
                    | 
                    <button type='button' className='btn btn-link' onClick={showUpcomingAppointments}>
                        upcoming appointments only
                    </button> 
                    |
                    <button type='button' className='btn btn-link' onClick={showPastAppointments}>
                        past appointments only
                    </button>
                </h5>
                <table className='table'>
                    <thead>
                        <tr>
                            <th>date/time</th>
                            <th>client</th>
                            <th>service</th>
                            <th>employee</th>
                            <th>confirmation status</th>
                            <th>completion status</th>
                        </tr>
                        <tr>
                            <th><input onChange={handleDateFilterChange} placeholder='search by date' /></th>
                            <th><input onChange={handleClientFilterChange} placeholder='search by client' /></th>
                            <th><input onChange={handleServiceFilterChange} placeholder='search by service' /></th>
                            <th><input onChange={handleEmployeeFilterChange} placeholder='search by employee' /></th>
                            <th></th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                    {dateFilter.map(appointment => (
                        <tr key={appointment.id}>
                            <td>{formattedDateTime(appointment.start_time)}</td>
                            <td>{getClientName(appointment.client_id)}</td>
                            <td>{getServiceName(appointment.service_id)}</td>
                            <td>{getEmployeeName(appointment.employee_id)}</td>
                            <td>{confirmStatus(appointment.is_confirmed)}</td>
                            <td>{checkoutStatus(appointment.is_complete)}</td>
                        </tr>
                    )).reverse()}
                    </tbody>
                </table>
            </div>
        </>
    )
}
export default SearchAppointments

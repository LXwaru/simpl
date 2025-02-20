import { useState, useEffect } from 'react'
import Flatpickr from "react-flatpickr";
import "flatpickr/dist/themes/material_green.css"
import { useSelector, useDispatch } from 'react-redux'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'
import { updateUser } from '../../features/user/userSlice'



const CreateAppointment = () => {
    const user = useSelector((state) => state.user.value)
    const companyId = user.company.id
    const employees = user.company.employees
    const services = user.company.services
    const clients = user.company.clients
    const appointments = user.company.appointments
    const [ employeeId, setEmployeeId ] = useState('')
    const [ serviceId, setServiceId ] = useState('')
    const [ clientId, setClientId ] = useState(0)
    const [ creditId, setCreditId ] = useState(0)
    const [ credits, setCredits ] = useState([])
    const [ date, setDate ] = useState(null)
    const handleEmployeeChange = (e) => setEmployeeId(e.target.value)
    const handleServiceChange = (e) => setServiceId(e.target.value)
    const handleClientChange = (e) => setClientId(e.target.value)
    const handleCreditChange = (e) => setCreditId(e.target.value)
    const navigate = useNavigate()
    const dispatch = useDispatch()
    
    const formatDate = (rawDate) => {
        const localDate = new Date(rawDate)
        const UTCDate = localDate.toISOString()
        return UTCDate
    }


    const findConflicts = (clientId, employeeId, serviceId, date) => {
        const selectedService = services.find(service => service.id === parseInt(serviceId, 10))
        const serviceDuration = selectedService.duration
        const serviceStartTime = selectedService.start_time
        const employeeConflict = appointments.filter(appointment => {
            appointment.employee_id === employeeId &&
            appointment.start_time < serviceDuration &&
            appointment.start_time > serviceDuration
        })
    }

    useEffect(() => {
        const fetchCredits = () => {
            if (!clientId && !serviceId) {
                return
            }
            try {
                const client = clients.find((client) => client.id === parseInt(clientId, 10))
                const clientCredits = client.credits
                const filteredCredits = clientCredits.filter((credits) => credits.service_id === parseInt(serviceId, 10))
                setCredits(filteredCredits)
            } catch (error) {
                console.error('cannot fetch credits', error)
            }
        }
        fetchCredits()
    }, [clientId, serviceId])
    

    const handleSubmit = async (e) => {
        e.preventDefault()
        if (!clientId || !serviceId || !employeeId || !date) {
            alert('client, service, employee AND date must be selected')
            return
        }

        try {
            const payload = {
                client_id: clientId,
                service_id: serviceId,
                employee_id: employeeId,
                credit_id: creditId,
                start_time: formatDate(date)
            }
            await axios.post(`http://localhost:8000/api/${companyId}/appointments/`, payload, {
                withCredentials: true
            })
            alert('appointment created successfully')
            navigate('/dashboard')
        

            const { data: updatedUser } = await axios.get(`http://localhost:8000/users/me`, {
                withCredentials: true
            })

            dispatch(updateUser(updatedUser))
        } catch (error) {
            console.error('could not make reservation', error)
        }
    }
    

    return (
        <>
            <div className='form-control'>
                <h3>create an appointment</h3>
                <form onSubmit={handleSubmit}>
                    <select 
                        onChange={handleClientChange}
                        className="form-select form-select-sm" 
                        aria-label="Small select example"
                        defaultValue=''
                    >
                        <option value='' disabled>select a client</option>
                    {clients.map((client) => (
                        <option key={client.id} value={client.id}>{client.full_name}</option>
                    ))}
                    </select>
                    <select 
                    onChange={handleServiceChange}
                    className="form-select form-select-sm" 
                    aria-label="Small select example"
                    defaultValue=''>
                        <option value='' disabled>select a service</option>
                    {services.map((service) => (
                        <option key={service.id} value={service.id}>{service.title}</option>
                    ))}
                    </select>
                    <select
                    onChange={handleEmployeeChange}
                    className="form-select form-select-sm" 
                    aria-label="Small select example"
                    defaultValue=''>
                        <option value='' disabled>select an employee</option>
                    {employees.map((employee) => (
                        <option key={employee.id} value={employee.id}>{employee.full_name}</option>
                    ))}
                    </select>
                    <h5>choose a date and time</h5>
                    <Flatpickr
                    placeholder='click here'
                    value={date}
                    onChange={(date) => setDate(date)}
                    options={{
                        enableTime: true,
                        minTime: "9:00",
                        maxTime: "17:00",
                        minuteIncrement: 15,
                        dateFormat: 'D, m/d/Y, H:i'
                    }}
                    /> <br />
                    <button className='btn btn-success'>submit</button>
                </form>
            </div>
        </>
    )
}
export default CreateAppointment
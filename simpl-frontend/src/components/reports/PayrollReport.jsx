import { useState, useEffect } from 'react'
import { useSelector } from 'react-redux'
import Flatpickr from "react-flatpickr";
import "flatpickr/dist/themes/material_green.css"
import axios from 'axios'


const GenerateReport = ({ dateRange, employeeId, employees }) => {
    const user = useSelector((state) => state.user.value)
    const companyId = user.company.id
    const [ appointmentFilter, setAppointmentFilter ] = useState([])
    const employee = employees.find((employee) => employee.id === parseInt(employeeId, 10))
    const [ startDate, setStartDate ] = useState('')
    const [ endDate, setEndDate ] = useState('')
    const services = user.company.services
    const clients = user.company.clients
    const [ loading, setLoading ] = useState(false)
    const [ total, setTotal ] = useState(0)


    const getClientName = (clientId) => {
        const client = clients.find((client) => client.id === parseInt(clientId, 10))
        return client.full_name
    }

    const getPayRate = (employeeId, serviceId) => {
        const employee = employees.find((employee) => employee.id === parseInt(employeeId, 10))
        const payRates = employee.pay_rates
        const payRate = payRates.find((rate) => 
            rate.employee_id === parseInt(employeeId, 10) &&
            rate.service_id === parseInt(serviceId, 10))
            return payRate ? payRate.rate_per_service : null
        }

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
        return `${dayOfWeek}, ${formattedDate} - ${formattedTime}`
    }

    const getServiceName = (serviceId) => {
        const service = services.find((service) => service.id === parseInt(serviceId, 10))
        return service.title
    }

    const filterAppointments = () => {
        if (!employee || !startDate || !endDate) {
            return
        }
        if (employeeId && dateRange.length === 2) {
            try {
                setLoading(true)
                const filter = employee.appointments.filter((appointment) => 
                    appointment.credit.completed_on > startDate &&
                    appointment.credit.completed_on < `${endDate}T23:59:00000`
            )
            setAppointmentFilter(filter)
            } catch (error) {
                console.error('could not fetch appointments', error)
            } finally {
                setLoading(false)
            }
        }
    }


    const getTotal = async (appointments) => {
        if (!appointments){
            return
        }
        let totalPay = 0
        for (let appointment of appointments) {
            let serviceId = appointment.service_id
            let employeeId = appointment.employee_id
            try {
                setLoading(true)
                let payRateResponse = await axios.get(`http://localhost:8000/api/${companyId}/pay_rate/${employeeId}/${serviceId}/`, {
                    withCredentials: true
                })
                let payRateResponseData = payRateResponse.data
                let ratePerService = payRateResponseData.rate_per_service
                totalPay += ratePerService
                setTotal(totalPay)
                
            } catch (error) {
                console.error('could not calculate payroll', error)
            } finally {
                setLoading(false)
            }
        }
    }
    
    useEffect(() => {
        getTotal(appointmentFilter)
    }, [appointmentFilter])



    useEffect(() => {
        if (dateRange[0] && dateRange[1]) {
            const formattedStartDate = dateRange[0].toISOString()
            const formattedEndDate = dateRange[1].toISOString()
            setStartDate(formattedStartDate)
            setEndDate(formattedEndDate)
        }
    }, [dateRange])

    useEffect(() => {
        if (startDate && endDate && employee) {
            filterAppointments()
        }
    }, [employee, startDate, endDate])

    if (loading) {
        return <div>loading...</div>
    }

    return (
        <>
            {employee? (
                <div>
                    <h3>{employee.full_name}</h3>
                    <h5>pay for specified date range:</h5>
                    <p>${total}</p>
                    <table className='table'>
                        <thead>  
                            <tr>
                                <th>date completed</th>
                                <th>service</th>  
                                <th>client</th>
                                <th>wage</th>
                            </tr>
                        </thead>
                        <tbody>
                            {appointmentFilter.map((appointment) => (
                                <tr key={appointment.id}>
                                    <td>{formattedDateTime(appointment.credit.completed_on)}</td>
                                    <td>{getServiceName(appointment.service_id)}</td>
                                    <td>{getClientName(appointment.client_id)}</td>
                                    <td>${getPayRate(appointment.employee_id, appointment.service_id)}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>    
                </div>


            ) : (
                <h3>select an employee</h3>
            )}

        </>
    )
}


const PayrollReport = () => {
    const user = useSelector((state) => state.user.value)
    const [ dateRange, setDateRange ] = useState([])
    const [ employeeId, setEmployeeId ] = useState(0)
    const employees = user.company.employees

    const handleEmployeeChange = (e) => {
        setEmployeeId(e.target.value)
    }
    
    let days
    
    return (
        <>
            <div className='form-control container-l'>
                <h3>payroll report</h3>
                <table className='table'>
                    <thead>
                        <tr>
                            <th>choose date range</th>
                            <th>select employee</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                                <Flatpickr
                                    placeholder='click here'
                                    value={dateRange}
                                    onChange={(days) => setDateRange(days)}
                                    options={{
                                        mode: 'range',
                                        dateFormat: 'm/d/y'
                                    }}
                                    />
                            </td>
                            <td>
                            <select
                            onChange={handleEmployeeChange}
                            className="form-select form-select-sm" 
                            aria-label="Small select example"
                            defaultValue=''>
                                <option value='' disabled>select employee</option>
                            {employees.map((employee) => (
                                <option key={employee.id} value={employee.id}>{employee.full_name}</option>
                            ))}
                            </select>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
                <div className='form-control'>
                    <GenerateReport 
                        employeeId={employeeId}
                        employees={employees}
                        dateRange={dateRange}
                    />
                </div>
        </>
    ) 
}
export default PayrollReport





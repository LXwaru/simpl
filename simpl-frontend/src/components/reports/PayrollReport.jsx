import { useState } from 'react'
import axios from 'axios'
import { useSelector, useDispatch } from 'react-redux'
import { setUser } from '../../features/user/userSlice'
import Flatpickr from "react-flatpickr";
import "flatpickr/dist/themes/material_green.css"



const PayrollReport = () => {
    const [ startDate, setStartDate ] = useState('')
    const [ endDate, setEndDate ] = useState('')
    const [ employeeId, setEmployeeId ] = useState(0)
    const user = useSelector((state) => state.user.value)
    const allAppointments = user.company.appointments
    const [ appointmentFilter, setAppointmentFilter ] = useState([])
    const [ loading, setLoading ] = useState(false)
    const employees = user.company.employees
    const services = user.company.services
    const clients = user.company.clients



    const handleEmployeeChange = (e) => {
        setEmployeeId(e.target.value)
    }

    const getServiceName = (serviceId) => {
        const service = services.find((service) => service.id === parseInt(serviceId, 10))
        return service.title
    }

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
    

    const GenerateReport = (startDate, endDate, clientId) => {
        const employee = employees.find((employee) => employee.id === parseInt(employeeId, 10))
        return (
            <>
                {employee? (
                    <div>

                        <h3>{employee.full_name}</h3>
                        <table className='table'>
                            <thead>
                                <tr>
                                    <th>date</th>
                                    <th>service</th>
                                    <th>client</th>
                                    <th>wage</th>
                                </tr>
                            </thead>
                            <tbody>
                                {employee.appointments.map((appointment) => (
                                    <tr key={appointment.id}>
                                        <td>{appointment.start_time}</td>
                                        <td>{getServiceName(appointment.service_id)}</td>
                                        <td>{getClientName(appointment.client_id)}</td>
                                        <td>{getPayRate(appointment.employee_id, appointment.service_id)}</td>
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

    if (loading) {
        return <div>loading...</div>
    }

    return (
        <>
            <div className='form-control'>
                <h3>payroll report</h3>
                <table className='table'>
                    <thead>
                        <tr>
                            <th>choose starting date</th>
                            <th>choose ending date</th>
                            <th>select employee</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                                <Flatpickr
                                placeholder='click here'
                                value={startDate}
                                onChange={(startDate) => setStartDate(startDate)}
                                options={{
                                    enableTime: true,
                                    minTime: "9:00",
                                    maxTime: "17:00",
                                    minuteIncrement: 15,
                                    dateFormat: 'D, m/d/Y, H:i'
                                }}
                                />
                            </td>
                            <td>
                                <Flatpickr
                                    placeholder='click here'
                                    value={endDate}
                                    onChange={(endDate) => setEndDate(endDate)}
                                    options={{
                                        enableTime: false,
                                        dateFormat: 'D, m/d/Y'
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
                    <GenerateReport />
                </div>
        </>
    ) 
}
export default PayrollReport
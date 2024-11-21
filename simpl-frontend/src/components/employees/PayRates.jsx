import axios from 'axios'
import { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'
import { updateUser } from '../../features/user/userSlice'
import { Link, useNavigate } from 'react-router-dom'

const PayRates = () => {
    const {id} = useParams()
    const user = useSelector((state) => state.user.value)
    const companyId = user.company.id
    const employees = user.company.employees
    const employee = employees.find((employee) => employee.id === parseInt(id, 10))
    const payRates = employee.pay_rates
    const services = user.company.services

    const fetchPayRate = (serviceId) => {
        const payRate = payRates.find((payRate) => payRate.service_id === serviceId)
        return payRate.rate_per_service
    }

    console.log(payRates)
    return (
        <>
            <p>{employee.full_name}</p>
            <table className='table'>
                <thead>
                    <tr>
                        <th>service title</th>
                        <th>current pay rate</th>
                        <th>establish or update</th>
                    </tr>
                </thead>
                <tbody>
            {services.map((service) => (
                <tr key={service.id}>
                    <td>{service.title}</td>
                    <td>${fetchPayRate(service.id)}</td>
                </tr>
            ))}

                </tbody>
            </table>
        </>
    )
}
export default PayRates
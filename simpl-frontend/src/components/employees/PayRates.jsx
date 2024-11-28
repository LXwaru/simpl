import axios from 'axios'
import { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'
import { updateUser } from '../../features/user/userSlice'
import { Link, useNavigate } from 'react-router-dom'

const PayRates = () => {
    const {id} = useParams()
    const dispatch = useDispatch()
    const user = useSelector((state) => state.user.value)
    const companyId = user.company.id
    const employees = user.company.employees
    const employee = employees.find((employee) => employee.id === parseInt(id, 10))
    const payRates = employee.pay_rates
    const services = user.company.services
    const [ rate, setRate ] = useState(0)
    const [ loading, setLoading ] = useState(false)

    const fetchPayRate = (serviceId) => {
        const payRate = payRates.find((payRate) => payRate.service_id === serviceId)
        if (!payRate) {
            return <p><i>'rate not established'</i></p>
        } else {
            const ratePerService = payRate.rate_per_service
            return <p>{`$${ratePerService }`}</p>
        }
    }


    const handleRateChange = (e) => {setRate(e.target.value)}

    const checkRate = async (serviceId) => {
        const service = services.find((service) => service.id === parseInt(serviceId, 10))
        if (rate >= service.price) {
            alert('rate must be less than gross price')
            return
        }
        const payRate = payRates.find((payRate) => payRate.service_id === serviceId)
        if (payRate) {
            try {
                setLoading(true)

                const payload = {
                    employee_id: id,
                    service_id: serviceId,
                    rate_per_service: rate
                }
                await axios.put(`http://localhost:8000/api/${companyId}/pay_rate/`, payload, {
                    withCredentials: true
                })
            } catch (error) {
                console.error('could not update rate', error)
            } finally {
                const { data: updatedUser } = await axios.get(`http://localhost:8000/users/me`, {
                    withCredentials: true
                })
                dispatch(updateUser(updatedUser))
                setLoading(false)
            }
        } else {
            try {
                setLoading(true)
                const payload = {
                    employee_id: id,
                    service_id: serviceId,
                    rate_per_service: rate
                }
                await axios.post(`http://localhost:8000/api/${companyId}/pay_rates/`, payload, {
                    withCredentials: true
                })

            } catch (error) {
                console.error('could not register rata', error)
            } finally {
                const { data: updatedUser } = await axios.get(`http://localhost:8000/users/me`, {
                    withCredentials: true
                })
    
                dispatch(updateUser(updatedUser))
                setLoading(false)
            }

        }
    }

    if (loading) {
        return <h3>Loading...</h3>
    }

    return (
        <>
                <h3>{employee.full_name}</h3>
                <table className='table'>
                    <thead>
                        <tr>
                            <th>service title</th>
                            <th>gross per service</th>
                            <th>current pay rate</th>
                            <th>establish or update</th>
                        </tr>
                    </thead>
                    <tbody>
                    {services.map((service) => (
                        <tr key={service.id}>
                            <td>{service.title}</td>
                            <td>${service.price}</td>
                            <td>{fetchPayRate(service.id)}</td>
                            <td>
                                <div className='form-floating mb-3'>
                                    <input onChange={handleRateChange} type="number" className="form-control" id="rate" placeholder="rate" />
                                    <label htmlFor="rate">new rate</label>
                                </div>
                            </td>
                            <td><button className='btn btn-success' type='submit' onClick={() => checkRate(service.id)}>save new rate</button></td>
                        </tr>
                    ))}
                    </tbody>
                </table>
        </>
    )
}
export default PayRates
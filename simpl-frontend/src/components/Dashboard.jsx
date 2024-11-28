import { useEffect, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import axios from 'axios'
import { useSelector, useDispatch } from 'react-redux'
import { setUser } from '../features/user/userSlice'
import AppointmentDashboard from './appointments/appointmentDashboard'

const Dashboard = () => {
    const user = useSelector((state) => state.user.value)
    const dispatch = useDispatch()
    const [ loading, setLoading ] = useState(true)
    const [ creditId, setCreditId ] = useState()
    const navigate = useNavigate()

    
    useEffect(() => {
        const getData = async () => {
            try {
                setLoading(true)
                const response = await axios.get('http://localhost:8000/users/me', {
                    withCredentials: true
                })
                if (user === null) {
                    navigate('/')
                    return
                }
                dispatch(setUser(response.data))
            } catch (error) {
                console.error('failed to fetch user data', error)
            } finally {
                setLoading(false)
            }
        }
        getData()
    }, [dispatch])

    if (loading) {
        return <div>loading...</div>
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
    const getEmployeeName = (employeeId) => {
        const employees = user.company.employees
        const employee = employees.find((employee) => employee.id === parseInt(employeeId, 10))
        return employee.full_name
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


    return (
        <>
            {user.company ? (
                <div>
                    <h3>{user.company.name}</h3>
                    <p>{user.company.description}</p>
                    <AppointmentDashboard />
                </div>
            ) : (
                <h3>{user.username}</h3>
            )}
        </>
    )
}
export default Dashboard
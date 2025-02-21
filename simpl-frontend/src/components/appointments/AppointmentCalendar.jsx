import { useEffect, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import axios from 'axios'
import { useSelector, useDispatch } from 'react-redux'
import { updateUser } from '../../features/user/userSlice'
import { Calendar, momentLocalizer } from 'react-big-calendar'
import moment from 'moment'
import 'react-big-calendar/lib/css/react-big-calendar.css'


const AppointmentCalendar = () => {
    const user = useSelector((state) => state.user.value)
    const appointments = user.company.appointments
    const services = user.company.services
    const clients = user.company.clients
    const employees = user.company.employees    
    const localizer = momentLocalizer(moment)   
    const events = appointments.map((appointment) => {
        const service = services.find((service) => service.id === appointment.service_id)
        const client = clients.find((client) => client.id === appointment.client_id)
        const employee = employees.find((employee) => employee.id === appointment.employee_id)
        return {
            title: client.full_name + ' - (' + service.title + ' with ' + employee.full_name + ')',
            start: new Date(appointment.start_time),
            end: new Date(appointment.end_time),
        }
    })

    return (
        <>
            {appointments.length > 0 ? (
                <div>
                    <h3>appointments</h3>
                    <Calendar
                        localizer={localizer}
                        events={events}
                        titleAccessor="title"
                        startAccessor="start"
                        endAccessor="end"
                        style={{ width: '100%', height: '500px' }}
                        defaultView='day'
                    />
                </div>
            ) : (
                <div>
                    <h3>the calendar is empty</h3>
                </div>
            )}
        </>
    )
}

export default AppointmentCalendar
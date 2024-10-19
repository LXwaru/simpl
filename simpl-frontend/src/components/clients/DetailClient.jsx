import { useParams } from 'react-router-dom'
import axios from 'axios'
import { useSelector, useDispatch } from 'react-redux'
import { updateUser } from '../../features/user/userSlice'
import { Link, useNavigate } from 'react-router-dom'

const DetailClient = () => {

    const {id} = useParams()
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const user = useSelector((state) => state.user.value)
    const company_id = user.company.id
    const clients = user.company.clients
    const client = clients.find((client) => client.id === parseInt(id, 10))
    const credits = client.credits
    const activeCredits = credits.filter((credit) => credit.is_active === true)
    const unpaidCredits = credits.filter((credit) => credit.is_active === false)
    const finishedCredits = credits.filter((credit) => credit.is_complete === true)
    const appointments = client.appointments
    const incompleteAppointments = appointments.filter((appointment) => appointment.is_complete === false)


    return (
        <>
            <div className='container-fluid form-control'>
                <h3>client details</h3><hr />
                <p><strong>client name: </strong>{client.full_name}</p>
                <p><strong>client email: </strong><Link to={`mailto:${client.email}`}>{client.email}</Link></p>

                <div className="accordion" id="credits">
                    <div className="accordion-item">
                        <h2 className="accordion-header">
                        <button className="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                            <strong>active credits: {activeCredits.length}</strong> 
                        </button>
                        </h2>
                        <div id="collapseOne" className="accordion-collapse collapse" data-bs-parent="#credits">
                            <div className="accordion-body">                           
                            {activeCredits.map((credit) => (
                            <ul className='list-group' key={credit.id}>
                                <li className='list-group-item'>{credit.service_title}</li>
                            </ul>
                        ))}
                            </div>
                        </div>
                    </div>
                    <div className="accordion-item">
                        <h2 className="accordion-header">
                        <button className="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                            <strong>unpaid credits: {unpaidCredits.length}</strong>
                        </button>
                        </h2>
                        <div id="collapseTwo" className="accordion-collapse collapse" data-bs-parent="#credits">
                            <div className="accordion-body">                           
                            {unpaidCredits.map((credit) => (
                            <ul className='list-group' key={credit.id}>
                                <li className='list-group-item'>{credit.service_title}</li>
                            </ul>
                        ))}
                            </div>
                        </div>
                    </div>
                    <div className="accordion-item">
                        <h2 className="accordion-header">
                        <button className="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                            <strong>service history: {finishedCredits.length} services rendered</strong>
                        </button>
                        </h2>
                        <div id="collapseThree" className="accordion-collapse collapse" data-bs-parent="#credits">
                            <div className="accordion-body">                           
                            {finishedCredits.map((credit) => (
                            <ul className='list-group' key={credit.id}>
                                <li className='list-group-item'>{credit.service_title}</li>
                            </ul>
                        ))}
                            </div>
                        </div>
                    </div>
                    <div className="accordion-item">
                        <h2 className="accordion-header">
                        <button className="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseFour" aria-expanded="false" aria-controls="collapseFour">
                            <strong>future or missed appointments: {incompleteAppointments.length} </strong>
                        </button>
                        </h2>
                        <div id="collapseFour" className="accordion-collapse collapse" data-bs-parent="#credits">
                            <div className="accordion-body">                           
                            {incompleteAppointments.map((appointment) => (
                            <ul className='list-group' key={appointment.id}>
                                <li className='list-group-item'>{appointment.service_id}</li>
                                <li className='list-group-item'>{appointment.start_time}</li>
                                <li className='list-group-item'>{appointment.employee_id}</li>
                            </ul>
                        ))}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}
export default DetailClient
import { setUser, updateUser } from "../../features/user/userSlice"
import { useSelector, useDispatch } from 'react-redux'
import { Link, useNavigate } from 'react-router-dom'
import axios from 'axios'

const ListClients = () => {
    
    const user = useSelector((state) => state.user.value)
    const company_id = user.company.id
    const clients = user.company.clients
    return (
        <>
            <div className="container-fluid form-control">
                <h3>clients</h3>
                <Link className='btn btn-link' to='/create-client'>register new client</Link>
                <table className='table'>
                    <thead>
                        <tr>
                            <th>client name</th>
                            <th>client email</th>
                        </tr>
                    </thead>
                    <tbody>
                        {clients.map((client) => (
                            <tr key={client.id}>
                                <td>{client.full_name}</td>
                                <td><Link to={`mailto:${client.email}`}>{client.email}</Link></td>
                                <td><Link to={`/detail-client/${client.id}`}>see client details...</Link></td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </>
    )
}
export default ListClients
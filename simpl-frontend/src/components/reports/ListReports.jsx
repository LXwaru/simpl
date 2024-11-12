import { Link } from 'react-router-dom'



// what reports are needed?
// filterable sales, filterable appointments, payroll (employee rates per service 
// needs to be setup), 
const ListReports = () => {
    return (
        <>
            <ul className='list-group'>
                <li className='list-group-item'><Link to='/list-sales'>list sales</Link></li>
                <li className='list-group-item'><Link to='/list-appointments'>list appointments</Link></li>
            </ul>
            
            
        </>
    )
}
export default ListReports
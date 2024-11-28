import { Link } from 'react-router-dom'



// what reports are needed?
// filterable sales, filterable appointments, payroll (employee rates per service 
// needs to be setup), 
const ListReports = () => {
    return (
        <>
            <ul className='list-group'>
                <li className='list-group-item'><Link to='/search-sales'>search sales</Link></li>
                <li className='list-group-item'><Link to='/search-appointments'>search appointments</Link></li>
                <li className='list-group-item'><Link to='/payroll-report'>payroll report</Link></li>
                <li className='list-group-item'>sales report</li>
            </ul>
            
            
        </>
    )
}
export default ListReports
import { useSelector } from 'react-redux'
import { Link } from 'react-router-dom'

const ListEmployees = () => {
    const user = useSelector((state) => state.user.value)
    const employees = user.company.employees
    return (
        <>
            <div className='form-control'>
                <h3>Employees</h3>
                <Link className='btn btn-link' to='/create-employee'>register a new employee</Link>
                <table className='table'>
                    <thead>
                        <tr>
                            <th>name</th>
                            <th>email</th>
                        </tr>
                    </thead>
                    <tbody>
                        {employees.map((employee) => (
                        <tr key={employee.id}>
                            <td>{employee.full_name}</td>
                            <td>{employee.email}</td>
                            <td><Link to={`/detail-employee/${employee.id}`}>see employee details...</Link></td>
                        </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </>
    )
}
export default ListEmployees
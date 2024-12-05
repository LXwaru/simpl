import { Link } from 'react-router-dom'
import { useSelector } from 'react-redux'
import { useState } from 'react'

const SearchSales = () => {
    const user = useSelector((state) => state.user.value)
    const sales = user.company.sales
    const [ nameFilterValue, setNameFilterValue ] = useState('')
    const [ dateFilterValue, setDateFilterValue ] = useState('')


const formatDateTime = (date) => {
    const formattedDate = new Date(date)
    const month = String(formattedDate.getMonth() + 1).padStart(2, '0')
    const day = String(formattedDate.getDate()).padStart(2, '0')
    const year = formattedDate.getFullYear()
    const hours = String(formattedDate.getHours()).padStart(2, '0')
    const minutes = String(formattedDate.getMinutes()).padStart(2, '0')
    return `${month}/${day}/${year}`
}


    const nameFilter = sales.filter((sale) => sale.client_name.toLowerCase().includes(nameFilterValue.toLowerCase()))
    
    const nameDateFilter = nameFilter.filter((sale) => {
        const formattedSaleDate = formatDateTime(sale.date)
        return formattedSaleDate.includes(dateFilterValue)
    })


    const handleNameFilterChange = (e) => {setNameFilterValue(e.target.value)}
    const handleDateFilterChange = (e) => {setDateFilterValue(e.target.value)}


    return (
        <>
            <div className='form-control'>
                <h3>sales search</h3>
                <table className='table'>
                    <thead>
                        <tr>
                            <th>sale id</th>
                            <th><br />sale date</th>
                            <th>client name - 
                            </th>
                            <th>total amount</th>
                            <th>more information</th>
                        </tr>
                        <tr>
                            <th></th>
                            <th><input onChange={handleDateFilterChange} placeholder='date lookup' /></th>
                            <th><input onChange={handleNameFilterChange} placeholder="filter by client name" /></th>
                        </tr>
                    </thead>
                    <tbody>
                        {nameDateFilter.map(sale => (
                        <tr key={sale.id}>
                            <td>{sale.id}</td>
                            <td>{formatDateTime(sale.date)}</td>
                            <td>{sale.client_name}</td>
                            <td>${sale.total_due}</td>
                            <td>
                                <Link to={`/detail-sale/${sale.id}`}>sale details</Link>
                            </td>
                        </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </>
    )
}
export default SearchSales
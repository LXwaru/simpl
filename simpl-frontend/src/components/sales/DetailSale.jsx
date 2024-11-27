import axios from 'axios'
import { useSelector, useDispatch } from 'react-redux'
import { updateUser } from '../../features/user/userSlice'
import { useState, useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'

const DetailSale = () => {
    const {id} = useParams()
    const user = useSelector((state) => state.user.value)
    const sales = user.company.sales
    const sale = sales.find((sale) => sale.id === parseInt(id, 10))

    const redeemStatus = (isRedeemed) => {
        if (isRedeemed) {
            return 'redeemed'
        } else {
            return 'not redeemed'
        }
    }

    const dateFormat = (date) => {
        if (date) {
            const formatDate = new Date(date)
            return formatDate.toLocaleString()
        } else {
            return 'n/a'
        }
    }

    return (
        <>
            <div className='form-control'>
                <h3>sale information</h3>
                <table className='table'>
                    <thead>
                        <tr>
                            <th>company name</th>
                            <th>sale id</th>
                            <th>date/time of sale</th>
                            <th>client name</th>
                            <th>total</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>{user.company.name}</td>
                            <td>{sale.id}</td>
                            <td>{dateFormat(sale.date)}</td>
                            <td>{sale.client_name}</td>
                            <td>${sale.total_due}</td>
                        </tr>
                    </tbody>
                </table>
                <h3>service details</h3>
                <table className='table'>
                    <thead>
                        <tr>
                            <th>service title</th>
                            <th>price per service</th>
                            <th>status</th>
                            <th>date</th>
                        </tr>
                    </thead>
                    <tbody>
                        {sale.credits.map((item) => (
                            <tr key={item.id}>
                                <td>{item.service_title}</td>
                                <td>${item.price}</td>
                                <td>{redeemStatus(item.is_redeemed)}</td>
                                <td>{dateFormat(item.completed_on)}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
                <Link to='/list-sales'>return to sales list</Link>
            </div>
        </>
    )
}
export default DetailSale
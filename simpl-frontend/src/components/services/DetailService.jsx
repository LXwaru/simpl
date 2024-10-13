import { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import axios from 'axios'
import { useSelector, useDispatch } from 'react-redux'
import { Link } from 'react-router-dom'


const DetailService = () => {

    const {id} = useParams()

    const services = useSelector((state) => state.user.value.company.services)
    
    if (!services) {
        return <div>Loading services...</div>
    }
    const service = services.find((service) => service.id === parseInt(id, 10))



    return (
        <>
            <div className='form-control container-fluid'>
                <h3>{service.title} - ${service.price}</h3>
                <p>{service.description}</p>
                <button className='btn btn-light'>
                    <Link to='/create-sale'>purchase</Link>
                </button> <br />
                <button className='btn btn-light'>
                    <Link to='/create-appointment'>reserve</Link> <br />
                </button> <br />
                <button className='btn btn-light'>
                    <Link to='/list-services'>return to service list</Link>
                </button>

            </div>
        </>
    )
}
export default DetailService
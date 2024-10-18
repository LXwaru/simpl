import { Link, useNavigate, useParams } from 'react-router-dom'
import { useState, useEffect } from 'react'
import axios from 'axios'
import { useSelector, useDispatch } from 'react-redux'
import { setUser, updateUser } from '../../features/user/userSlice'



const EditService = () => {
    const {id} = useParams()
    const services = useSelector((state) => state.user.value.company.services)
    if (!services) {
        return <div>Loading services...</div>
    }
    const service = services.find((service) => service.id === parseInt(id, 10))
    const company_id = useSelector((state)=> state.user.value.company.id)
    const [ title, setTitle ] = useState(service.title)
    const [ price, setPrice ] = useState(service.price)
    const [ duration, setDuration ] = useState(service.duration)
    const [ description, setDescription ] = useState(service.description)
    const navigate = useNavigate()
    const dispatch = useDispatch()

    const handleTitleChange = (e) => {setTitle(e.target.value)}
    const handlePriceChange = (e) => {setPrice(e.target.value)}
    const handleDurationChange = (e) => {setDuration(`PT${e.target.value}M`)}
    const handleDescriptionChange = (e) => {setDescription(e.target.value)}

    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            const payload = {
                'title': title,
                'price': price,
                'duration': duration,
                'description': description
            }
            await axios.put(`http://localhost:8000/api/${company_id}/service/${id}/`, payload, {
                withCredentials: true
            })
            alert('service successfully updated')
            navigate(`/detail-service/${id}`)

            const { data: updatedUser } = await axios.get(`http://localhost:8000/users/me`, {
                withCredentials: true
            })

            dispatch(updateUser(updatedUser))
        } catch (error) {
            console.error('could not update service', error)
        }
    }

    return (
        <>
            <div className='container-fluid form-control'>
                <form onSubmit={handleSubmit}>
                    <h3>edit service: {service.title}</h3>
                    {/* title */}
                    <div className="form-floating mb-3">
                        <input onChange={handleTitleChange} type="text" className="form-control" id="title" placeholder={"title"} />
                        <label htmlFor="title">title</label>
                    </div>
                    {/* price */}
                    <div className="input-group mb-3">
                        <span className="input-group-text">$</span>
                        <div className="form-floating">
                            <input onChange={handlePriceChange} type="number" className="form-control" id="price" placeholder="price" />
                            <label htmlFor="price">price</label>
                        </div>
                    </div>
                    {/* duration */}
                    <div className="form-floating mb-3">
                        <input onChange={handleDurationChange} type="number" className="form-control" id="duration" placeholder="name@example.com" />
                        <label htmlFor="duration">duration in minutes</label>
                    </div>
                    {/* description */}
                    <div className="form-floating">
                        <textarea onChange={handleDescriptionChange} className="form-control" placeholder="service description" id="description"></textarea>
                        <label htmlFor="description">service description</label>
                    </div>
                    <button className='btn btn-primary'>submit</button>
                </form>
                <Link to='/list-services'>see all services</Link>
            </div>
        </>
    )
}
export default EditService
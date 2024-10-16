import { Link, useNavigate } from 'react-router-dom'

import { useState, useEffect } from 'react'
import axios from 'axios'
import { useSelector, useDispatch } from 'react-redux'





const CreateService = () => {
    const company_id = useSelector((state) => state.user.value.company.id) 
    const [ title, setTitle ] = useState('')
    const [ price, setPrice ] = useState(0)
    const [ duration, setDuration ] = useState('')
    const [ description, setDescription ] = useState('')
    const [ token, setToken ] = useState('')
    const navigate = useNavigate()


    // useEffect(() => {
    //     const getToken = async () => {
    //         try {
    //             const tokenResponse = await axios.get('http://localhost:8000/token')
    //             console.log(tokenResponse)
    //         } catch (error) {
    //             console.error('could not get access token', error)
    //         }
    //     }
    //     getToken()
    // }, [])

    
    const handleTitleChange = (e) => {
        setTitle(e.target.value)      
    } 

    const handlePriceChange = (e) => {
        setPrice(e.target.value)

    } 

    const handleDurationChange = (e) => {
        setDuration(`PT${e.target.value}M`)
    } 

    const handleDescriptionChange = (e) => {
        setDescription(e.target.value)
    } 

    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            const payload = {
                title: title,
                price: price,
                duration: duration,
                description: description
            }

            await axios.post(`http://localhost:8000/api/${company_id}/services`, payload, {
                withCredentials: true,
            })
            alert('service successfully registered')
            console.log("you finally did it you handsome son of a bitch")  
            navigate('/list-services')
        } catch (error){
            console.error("could not register service", error)
        }
    } 



    return (
        <>
            <div className='container-fluid form-control'>
                <form onSubmit={handleSubmit}>
                    <h3>register a new service</h3>
                    {/* title */}
                    <div className="form-floating mb-3">
                        <input onChange={handleTitleChange} type="text" className="form-control" id="title" placeholder="title" />
                        <label htmlFor="title">service title</label>
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
export default CreateService
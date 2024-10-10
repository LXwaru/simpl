import { useSelector, useDispatch } from 'react-redux'


const ListServices = () => {

    const user = useSelector((state) => state.user.value)    
    const services = user.company.services

    return (
        <>
            {services.map((service) => (
                <ul key={service.id}>
                    <div className='form-control'>
                        <li>{service.title}</li>
                        <li>{service.price}</li>
                        <li>{service.duration}</li>
                    </div>
                </ul>
            ))}
        </>
    )
}
export default ListServices
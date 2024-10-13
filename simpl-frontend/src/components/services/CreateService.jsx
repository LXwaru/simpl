import { Link } from 'react-router-dom'


const handleSubmit = () => {

}

const CreateService = () => {
    return (
        <>
            <Link to='/list-services'>see all services</Link>
            <div className='container-fluid form-control'></div>
                <form onSubmit={handleSubmit}>
                    {/* title, price, duration, description */}
                </form>
        </>
    )
}
export default CreateService
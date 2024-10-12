import { useSelector, useDispatch } from 'react-redux'
import { Link } from 'react-router-dom'



const ListServices = () => {

    const user = useSelector((state) => state.user.value)    
    const services = user.company.services


    const formatDuration = (isoDuration) => {
        // Use a regular expression to capture hours, minutes, and seconds
        const regex = /P(T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?)?/;
        const matches = isoDuration.match(regex);
        
        if (!matches) {
            return "Invalid duration format";
        }
    
        const hours = matches[2] ? parseInt(matches[2], 10) : 0;
        const minutes = matches[3] ? parseInt(matches[3], 10) : 0;
        const seconds = matches[4] ? parseInt(matches[4], 10) : 0;
        
        let result = '';
        
        if (hours) {
            result += `${hours} hour${hours > 1 ? 's' : ''} `
        }
        if (minutes) {
            result += `${minutes} minute${minutes > 1 ? 's' : ''} `;
        }
        if (seconds) {
            result += `${seconds} second${seconds > 1 ? 's' : ''}`;
        }
            
        return result.trim();
    }

    return (
        <>
            <div className='container-fluid'>
                <table className='table'>
                    <thead>
                        <tr>
                            <td>
                                <Link to='/'>register new service</Link>
                            </td>
                            <td>service title</td>
                            <td>price</td>
                            <td>duration</td>
                        </tr>
                    </thead>
                    <tbody>
                        {services.map((service) => (
                        <tr key={service.id}>
                            <td></td>
                            <td>{service.title}</td>
                            <td>{service.price}</td>
                            <td>{formatDuration(service.duration)}</td>
                        </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </>
    )
}
export default ListServices
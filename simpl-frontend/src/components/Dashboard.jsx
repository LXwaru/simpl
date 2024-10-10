import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'

const Dashboard = () => {
    const [ companyName, setCompanyName ] = useState('')
    const [ adminId, setAdminId ] = useState(0)

    
    useEffect(() => {
        const getData = async () => {
            const adminResponse = await axios.get('http://localhost:8000/users/me', {
                withCredentials: true
            })
            console.log(adminResponse.data.company.name)
            setCompanyName(adminResponse.data.company.name)
        }
        getData()
    }, [])

    return (
        <>
            <h3>{companyName}</h3>
        </>
    )
}
export default Dashboard
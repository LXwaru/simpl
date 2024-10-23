import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import { useSelector, useDispatch } from 'react-redux'
import { setUser } from '../features/user/userSlice'

const Dashboard = () => {
    const user = useSelector((state) => state.user.value)
    const dispatch = useDispatch()
    const [ loading, setLoading ] = useState(true)
    const navigate = useNavigate()

    
    useEffect(() => {
        const getData = async () => {
            try {
                setLoading(true)

                const response = await axios.get('http://localhost:8000/users/me', {
                    withCredentials: true
                })
                if (user === null) {
                    navigate('/')
                    return
                }
                dispatch(setUser(response.data))
            } catch (error) {
                console.error('failed to fetch user data', error)
            } finally {
                setLoading(false)
            }
        }
        getData()
    }, [dispatch])

    if (loading) {
        return <div>loading...</div>
    }

    return (
        <>
            {user.company ? (
                <div>
                    <h3>{user.company.name}</h3>
                    <p>{user.company.description}</p>
                </div>
            ) : (
                <h3>{user.username}</h3>
            )}
        </>
    )
}
export default Dashboard
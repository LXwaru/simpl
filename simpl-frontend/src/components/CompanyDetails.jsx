import { setUser } from '../features/user/userSlice'
import { useSelector, useDispatch } from 'react-redux'

const CompanyDetails = () => {
    const user = useSelector((state) => state.user.value)
    return (
        <>
            <h2>{user.company.description}</h2>
        </>
    )
}
export default CompanyDetails
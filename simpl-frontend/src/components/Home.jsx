import { useState, useEffect } from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

const Home = () => {
    const [ usertoken, setUsertoken  ] = useState('')
    return (
        <>
            <h1>[ s | b | s ]</h1>
            <h3>simpl business solutions</h3>
            <p>the simple solution for all of your merchant service needs</p>
        </>
    )
}
export default Home
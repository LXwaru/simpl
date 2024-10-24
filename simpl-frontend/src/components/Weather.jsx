import { useEffect, useState } from 'react'
import axios from 'axios'

const Weather = () => {
    const [ city, setCity ] = useState('')
    const [ weather, setWeather ] = useState('')
    const handleCityChange = (e) => {setCity(e.target.value)} 
    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            const weatherResponse = await axios.get(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=134f672d374105a6cdc3f2cdad855ca1`)
            const weatherData = weatherResponse.data.main
            console.log(weatherData)
            setWeather(weatherData)

        } catch (error) {
            console.error('could not get weather', error)
        }
    }
    

    const kelvinToFahrenheit = (temp) => {
        let value = (temp - 273.15) * 9/5 + 32
        return value.toFixed(0)
    }

    return (
        <>
            <form
            onSubmit={handleSubmit} 
            className='form-control'>

            <div className="form-floating mb-3">
                <input onChange={handleCityChange} type="text" className="form-control" id="city" placeholder="city" />
                <label htmlFor="city">enter city name</label>
                <button className='btn btn-light'>submit</button>
                {weather? (
                <div>
                    <p>the local weather is:</p>
                    <ul className='list-group'>
                        <li className='list-group-item'>current temp: {kelvinToFahrenheit(weather.temp)}</li>
                        <li className='list-group-item'>humidity: {weather.humidity}</li>
                        <li className='list-group-item'>feels like: {kelvinToFahrenheit(weather.feels_like)}</li>
                        <li className='list-group-item'>today's high: {kelvinToFahrenheit(weather.temp_max)}</li>
                        <li className='list-group-item'>today's low: {kelvinToFahrenheit(weather.temp_min)}</li>
                    </ul>
                </div>
                ) : (
                    <div>

                    </div>
                )}
            </div>
            </form>

        </>
    )
}
export default Weather
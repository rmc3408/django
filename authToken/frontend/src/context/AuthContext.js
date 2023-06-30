import { createContext, useState, useEffect } from 'react'
import jwt_decode from "jwt-decode";
import { useHistory } from 'react-router-dom'

const AuthContext = createContext()

export default AuthContext;


export const AuthProvider = ({children}) => {
    let [authTokens, setAuthTokens] = useState(() => JSON.parse(localStorage.getItem('authTokens')) ?? null)
    let [user, setUser] = useState(() => JSON.parse(localStorage.getItem('authTokens')) ?? null)
    let [loading, setLoading] = useState(true)

    const history = useHistory()

    let loginUser = async (e)=> {
        e.preventDefault()
        let response = await fetch('http://127.0.0.1:4000/api/token/', {
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify({'username':e.target.username.value, 'password':e.target.password.value})
        })
        let data = await response.json()

        if(response.status === 200){
            setAuthTokens(data)
            setUser(jwt_decode(data.access))
            localStorage.setItem('authTokens', JSON.stringify(data))
            history.push('/')
        }else{
            alert('Something went wrong!')
        }
    }


    let logoutUser = () => {
        setAuthTokens(null)
        setUser(null)
        localStorage.removeItem('authTokens')
        history.push('/login')
    }


    let updateToken = async ()=> {
        let response = await fetch('http://127.0.0.1:4000/api/token/refresh/', {
            method:'POST',
            headers:{
                'Content-Type':'application/json',
            },
            body: JSON.stringify({'refresh': authTokens?.refresh })
        })

        let data = await response.json()
        console.log(authTokens?.refresh, data)

        if (response.status === 200){
            setAuthTokens(data)
            setUser(jwt_decode(data.access))
            localStorage.setItem('authTokens', JSON.stringify(data))
        }else{
            logoutUser()
        }

        if(loading){
            setLoading(false)
        }
    }

    let contextData = {
        user: user,
        authTokens: authTokens,
        loginUser: loginUser,
        logoutUser: logoutUser,
    }


    useEffect(() => {

        if(loading){
            updateToken()
        }

        let fourMinutes = 1000 * 60 * 4

        let interval = setInterval(()=> {
            if(authTokens) {
                updateToken()
            }
        }, fourMinutes)

        return ()=> clearInterval(interval)

    }, [loading])

    return (
        <AuthContext.Provider value={contextData} >
            {loading ? null : children}
        </AuthContext.Provider>
    )
}

import axios from 'axios'
import { ACCESS_TOKEN } from './constants'

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL
})

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        if (token) {
            config.headers.Authorization = `Bearer ${token}`
            //esto es para interceptar todos los request y ponerles el token de autenticacion 
            //en los headers, asi no tenemos que escribirlo en el codigo cada vez que mandemos un request
            //ponele
        }        
        return config
    },    
    (error) => {        
        return Promise.reject(error);
    }
);


export default api;
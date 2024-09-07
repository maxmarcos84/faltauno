import { Component, useState } from "react"
import api from "../api"
import FormPlayer from "../components/FormPlayer"

function Home() {

    const[player, setPlayer] = useState('');

    //aca tengo que chequear si el usuario tiene player, si tiene cargo los datos del player aca mismo en home
    //si no tiene tengo que redirigir a la pagina que carga el formulario para crear el player

    const getPlayer = () =>{
        let user_id = localStorage.getItem('user_id')
        api.get("api/players/"+ user_id)
        .then((res) => res.data)
        .then((data)=>{
            setPlayer(data);
        })
        .catch((err)=> alert(err));
    }
    return (
        <>
        <div>Home</div>
        <FormPlayer></FormPlayer>
        </>    
    )
}

export default Home
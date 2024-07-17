import { Component, useState } from "react"
import api from "../api"
import Form from "../components/FormPlayer"

function Home() {

    const[player, setPlayer] = useState('');

    const getPlayer = () =>{
        api.get("api/players/")
        .then((res) => res.data)
        .then((data)=>{
            setPlayer(data);
        })
        .catch((err)=> alert(err));
    }
    return (
        <>
        <div>Home</div>
        <Form></Form>
        </>    
    )
}

export default Home
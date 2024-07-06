import { useState } from "react"
import api from "../api"

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
    return <div>Home</div>
}

export default Home
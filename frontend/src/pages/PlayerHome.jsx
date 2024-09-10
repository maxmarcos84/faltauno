import React, { useContext } from 'react';
import { PlayerContext } from '../PlayerContext';

function PlayerHome(){
    const { player } = useContext(PlayerContext);  // Accedemos al jugador desde el contexto
    
    const getSkills = async () => {
        try{
            const { data } = await api.get(`api/players/`+resp.data.user.id);

        }catch (err) {
            alert(`Error: ${err.message}`);
          }
    }

    return(
        <>
        <div>
            <h1>Bienvenido {player[0].nick_name}</h1>
            <h2>Nombre: {player[0].first_name}</h2>
            <h2>Apellido: {player[0].last_name}</h2>
            <h2>Deporte: {player[0].sport[0].name}</h2>
            

        </div>
        
        
        </>
    )
}

export default PlayerHome


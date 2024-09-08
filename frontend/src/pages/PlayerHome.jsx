import React, { useContext } from 'react';
import { PlayerContext } from '../PlayerContext';

function PlayerHome(){
    const { player } = useContext(PlayerContext);  // Accedemos al jugador desde el contexto

    console.log(player)

    if(!player){
        return <p> Creo que no hay player en contexto</p>;
    }
    

    return(
        <>
        <h1>Hola player</h1>
        <p> numbre: {player[0].nick_name}</p>
        </>
    )
}

export default PlayerHome


import { Component, useState, useEffect, useContext } from "react"
import { useNavigate } from 'react-router-dom';
import { PlayerContext } from "../PlayerContext";
import api from "../api"

function Home() {

    
    const navigate = useNavigate(); // Hook para redirigir

    useEffect(() => {
      // Llamamos a la función getPlayer al montar el componente
      getPlayer(navigate);
    }, [navigate]);

    const getPlayer = async (navigate) => {
        try {      
          // Verificar si la respuesta tiene contenido
          if (data) {
            setPlayer(data);
            console.log(34)
            navigate('/player_home'); // Redirigir a la página del jugador            
          } else {
            navigate('/create_player'); // Redirigir a la página del jugador
          }
        } catch (err) {
          alert(`Error: ${err.message}`);
        }
      };
      
    return (
        <>
        <div>Verificando...</div>
        </>    
    )
}

export default Home
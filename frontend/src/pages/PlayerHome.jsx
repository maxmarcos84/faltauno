import React, { useContext, useEffect, useState } from 'react';
import { PlayerContext } from '../PlayerContext';
import api from '../api';

function PlayerHome(){
    const { player } = useContext(PlayerContext);  // Accedemos al jugador desde el contexto
    const [skills, setSkills] = useState([]);
    
    const getSkills = async () => {
        try{
            const { data } = await api.get(`api/player_skills/${player[0].id}/`);
            setSkills(data);
        }catch (err) {
            alert(`Error: ${err.message}`);
          }
    };

    useEffect(() =>{
        if (player.length > 0){
            getSkills();
        }
    }, [player]);

    return(
        <>
        <div>
            <h1>Bienvenido {player[0].nick_name}</h1>
            <h2>Nombre: {player[0].first_name}</h2>
            <h2>Apellido: {player[0].last_name}</h2>
            <h2>Deporte: {player[0].sport[0].name}</h2>
        </div>
        <div>
            {skills.length > 0 ? (
            <table>
                <thead>
                <tr>
                    <th>Skill</th>
                    <th>Likes</th>
                    <th>Dislikes</th>
                </tr>
                </thead>
                <tbody>
                {skills.map((skill) => (
                    <tr key={skill.id}>
                    <td>{skill.skill_name}</td>
                    <td>{skill.like_count}</td>
                    <td>{skill.dislike_count}</td>
                    </tr>
                ))}
                </tbody>
            </table>
            ) : (
            <p>No hay habilidades registradas para este jugador.</p>
            )}
        </div>
            
        
        
        </>
    )
}

export default PlayerHome


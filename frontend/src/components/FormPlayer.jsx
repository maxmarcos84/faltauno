import { useState } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import "../styles/Form.css";

function Form(route){
    const [player, setPlayer] = useState("");
    const [name, setName] = useState("");
    const [lastName, setLastName] = useState("");
    
    return (
        <form className="form-container">
            <h1>Player</h1>
            <input 
            className="form-input"
            type="text" 
            placeholder="Nombre"           
            />
            <input 
            className="form-input"
            type="text" 
            placeholder="Apellido"           
            />
            <select placeholder="Deporte" className="form-select">
                <option value="futbol">Futbol</option>
                <option value="voley">Voley</option>
                <option value="padel">Padel</option>
            </select>
            <button className="form-button" type="submit">
                Enviar                
            </button>
        </form>

    );
}

export default Form;
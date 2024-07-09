import { useState } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import "../styles/Form.css";

function Form(route){
    const [player, setPlayer] = useState("");
    const [name, setName] = useState("");
    const [lastName, setLastName] = useState("");
    



    return (
        <form onSubmit={handleSubmit} className="form-container">
            <h1>Player</h1>
            <input 
            className="form-input"
            type="text"
            
            />

        </form>

    );
}

export default Form;
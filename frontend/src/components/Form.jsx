import { useState, useContext } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import { ACCESS_TOKEN, REFRESH_TOKEN, USER_ID } from "../constants";
import "../styles/Form.css";

//Lo nuevo
import { PlayerContext } from "../PlayerContext";
//

function Form({ route, method }) {
  //route es la ruta a donde nos redirige una vez que enviamos el form
  //method define si es login o registro
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  //nuevo
  const { setPlayer } = useContext(PlayerContext);  // Accedemos al contexto
//
  const name = method === "login" ? "Login" : "Register";

  const handleSubmit = async (e) => {
    setLoading(true);
    e.preventDefault();
    //removemos el comportamiento por default del formulario,
    //para evitar que se envie solo o se recargue la pagina cuando lo mandamos
    try {
      const resp = await api.post(route, { username, password });
      if (method === "login") {
        localStorage.setItem(ACCESS_TOKEN, resp.data.access);
        localStorage.setItem(REFRESH_TOKEN, resp.data.refresh);
        localStorage.setItem(USER_ID, resp.data.user.id);
        setPlayer(null);
        
        const { data } = await api.get(`api/players/`+resp.data.user.id);
        if (data) {
          console.log(data);
          setPlayer(data);
          navigate('/player_home'); // Redirigir a la página del jugador            
        } else {
          navigate('/create_player'); // Redirigir a la página del jugador
        }       
      } else { 
        navigate("/login");
      }
    } catch (error) {
      if (error.response && error.response.data) {
        Object.keys(error.response.data).forEach((field) => {
          const errorMessages = error.response.data[field];
          alert(errorMessages);
        });
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="form-container">
      <h1>{name}</h1>
      <input
        className="form-input"
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Username"
      />
      <input
        className="form-input"
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
      />
      <button className="form-button" type="submit">
        {name}
      </button>
    </form>
  );
}

export default Form;

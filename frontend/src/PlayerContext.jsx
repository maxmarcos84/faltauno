import React, { createContext, useState } from 'react';

// Creamos el contexto
export const PlayerContext = createContext();

// Proveedor del contexto que envuelve la aplicación
export const PlayerProvider = ({ children }) => {
  const [player, setPlayer] = useState(null);
  console.log("pasaste por el actualizador");

  return (
    <PlayerContext.Provider value={{ player, setPlayer }}>
      {children}
    </PlayerContext.Provider>
  );
};

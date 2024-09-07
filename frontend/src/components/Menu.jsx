import React from 'react';
import { AppBar, Toolbar, Typography, Button } from '@mui/material';
import { Link, Outlet } from 'react-router-dom';

const Navbar = () => {
  return (
    <div>
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" style={{ flexGrow: 1 }}>
          Mi Aplicación
        </Typography>
        <Button color="inherit" component={Link} to="/">Inicio</Button>
        <Button color="inherit" component={Link} to="/about">Acerca de</Button>
        <Button color="inherit" component={Link} to="/contact">Contacto</Button>
      </Toolbar>
    </AppBar>
    {/* Contenido dinámico debajo del menú */}
    <main className="content">
    <Outlet />
  </main>
  </div>
  );
};

export default Navbar;

import react from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { PlayerProvider } from "./PlayerContext";
import Navbar from "./components/Menu";
import Home from "./pages/Home";
import Login from "./pages/Login";
import NotFound from "./pages/NotFound";
import Register from "./pages/Register";
import ProtectedRoute from "./components/ProtectedRoute";
import CreatePlayer from "./pages/CreatePlayer";
import PlayerHome from "./pages/PlayerHome";

function Logout() {
  localStorage.clear();
  return <Navigate to="/login" />;
}

function RegisterAndLogout() {
  localStorage.clear();
  return <Register />;
}

function App() {
  return (
    <PlayerProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Navbar />}>            
            <Route
              path="/player_home"
              element={
                <ProtectedRoute>
                  <PlayerHome />
                </ProtectedRoute>
              }
            />
            <Route
              path="/create_player"
              element={
                <ProtectedRoute>
                  <CreatePlayer />
                </ProtectedRoute>
              }
            />            
            <Route path="/logout" element={<Logout />} />            
            <Route path="*" element={<NotFound />} />
          </Route>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<RegisterAndLogout />} />
        </Routes>
      </BrowserRouter>
    </PlayerProvider>
  );
}

export default App;

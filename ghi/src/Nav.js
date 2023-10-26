import { NavLink } from "react-router-dom";
import useToken from "@galvanize-inc/jwtdown-for-react";


function Nav() {
  const { logout } = useToken();


  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-success">
      <div className="container-fluid">
        <NavLink className="navbar-brand" to="/">
          Voy-Amie
        </NavLink>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav">
              <>
              <li className="nav-item">
                <NavLink className="nav-link" to="/">
                  Homepage
                </NavLink>
              </li>          
              <li className="nav-item">
                <NavLink className="nav-link" to="/profile">
                  Profile
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/finalized">
                  Itinerary
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/trips">
                  Create Trip
                </NavLink>
              </li>

              <li className="nav-item">
                <NavLink className="nav-link" to="/login">
                  Login
                </NavLink>
              </li>

              <li className="nav-item">
                <NavLink className="nav-link" to="/users">
                  Sign up
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/login" onClick={logout} >
                  Logout
                </NavLink>
              </li>            
              </>
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Nav;

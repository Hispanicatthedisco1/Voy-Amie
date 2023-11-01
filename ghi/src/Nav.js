import { NavLink } from "react-router-dom";
import useToken from "@galvanize-inc/jwtdown-for-react";
import { useEffect, useState } from "react";

function Nav() {
  const { logout } = useToken();
  const [user, setUser] = useState([]);
  const { token } = useToken();
  const getLoggedInUserData = async () => {
    const userUrl = `${process.env.REACT_APP_API_HOST}/token`;
    const response = await fetch(userUrl, {
      credentials: "include",
    });
    if (response.ok) {
      const userData = await response.json();
      setUser(userData);
    }
  };
  const userInfo = user?.user?.username;

  useEffect(() => {
    getLoggedInUserData();
  }, [token]); //eslint-disable-line react-hooks/exhaustive-deps
  return (
    <nav
      className="navbar navbar-expand-lg navbar-light"
      style={{ backgroundColor: "#29dde0" }}
    >
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
              {userInfo === undefined ? null : (
                <li className="nav-item">
                  <NavLink className="nav-link" to="/profile">
                    Profile
                  </NavLink>
                </li>
              )}
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
                <NavLink className="nav-link" to="/login" onClick={logout}>
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

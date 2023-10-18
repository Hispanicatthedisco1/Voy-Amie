import { useEffect, useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
// import Construct from "./Construct.js";
// import ErrorNotification from "./ErrorNotification";
import "./App.css";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import SignUpForm from "./SignUpForm.js";
import LoginForm from "./LogInForm.js";
import CreateTrip from "./CreateTripForm.js";
import Nav from "./Nav";
import UserProfileForm from "./UserProfileForm";

function App() {
  const domain = /https:\/\/[^/]+/;
  const basename = process.env.PUBLIC_URL.replace(domain, "");


  return (
    <div className="container">
      <BrowserRouter basename={basename}>
        <Nav />
          <AuthProvider baseUrl={process.env.REACT_APP_API_HOST}>
            <Routes>
              <Route exact path="/users" element= {<SignUpForm />}></Route>
              <Route exact path="/login" element={<LoginForm />}></Route>
              <Route exact path="/trips" element={ <CreateTrip /> }></Route>
              <Route exact path="/profile" element={ <UserProfileForm /> }></Route>
            </Routes>
          </AuthProvider>
      </BrowserRouter>
    </div>
  );
}

export default App;

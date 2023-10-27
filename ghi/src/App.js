import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import SignUpForm from "./SignUpForm.js";
import LoginForm from "./LogInForm.js";
import CreateTrip from "./CreateTripForm.js";
import Nav from "./Nav";
import UserProfileForm from "./UserProfileForm";
import TripsFinalized from "./TripFinalPage";
import TripDetail from "./TripDetailPage";
import CreateParticipants from "./Participants";
import Homepage from "./HomePage";

function App() {
  const domain = /https:\/\/[^/]+/;
  const basename = process.env.PUBLIC_URL.replace(domain, "");

  return (
    <div className="container">
      <BrowserRouter basename={basename}>
        <AuthProvider baseUrl={process.env.REACT_APP_API_HOST}>
          <Nav />
          <Routes>
            <Route exact path="/" element={<Homepage />}></Route>
            <Route exact path="/users" element={<SignUpForm />}></Route>
            <Route exact path="/login" element={<LoginForm />}></Route>
            <Route exact path="/trips" element={<CreateTrip />}></Route>
            <Route exact path="/finalized" element={<TripsFinalized />}></Route>
            <Route
              exact
              path="/trips/:trip_id/participants"
              element={<CreateParticipants />}
            ></Route>
            <Route
              exact
              path="/trips/:trip_id"
              element={<TripDetail />}
            ></Route>
            <Route
              exact
              path="/finalized/:trip_id"
              element={<TripsFinalized />}
            ></Route>
            <Route exact path="/profile" element={<UserProfileForm />}></Route>
          </Routes>
        </AuthProvider>
      </BrowserRouter>
    </div>
  );
}

export default App;

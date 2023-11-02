import { useState, useEffect } from "react";
import useToken from "@galvanize-inc/jwtdown-for-react";
import { Link, useNavigate } from "react-router-dom";


const UserProfileForm = () => {
  const [userIdInt, setUserIdInt] = useState(0);
  const [bio, setBio] = useState("");
  const [profile_pic, setProfilePic] = useState("");
  const [plannerTrips, setPlannerTrips] = useState([]);
  const [myTrips, setMyTrips] = useState([]);
  const [trip_query, setTripQuery] = useState("");
  const { token } = useToken();
  const navigate = useNavigate();

  const getUserData = async () => {
    const userUrl = `${process.env.REACT_APP_API_HOST}/token`;
    const response = await fetch(userUrl, {
      method: "GET",
      credentials: "include",
    });
    const userData = await response.json();
    console.log(userData);
    if (response.ok) {
      setUserIdInt(userData?.user.user_id);
      console.log(userIdInt)
      if (userData?.user.bio === null) {
        setBio("");
      } else {
        setBio(userData?.user.bio);
      }
      if (userData?.user.profile_pic === null) {
        setProfilePic("");
      } else {
        setProfilePic(userData?.user.profile_pic);
      }
    }
  };

  useEffect(() => {
    getUserData();
  }, [token]); //eslint-disable-line react-hooks/exhaustive-deps

  const getPlannerTripsData = async () => {
    const tripUrl = `${process.env.REACT_APP_API_HOST}/trips`;
    const response = await fetch(tripUrl, {
      credentials: "include",
    });

    if (response.ok) {
      const tripsData = await response.json();
      setPlannerTrips(tripsData);
    } else {
      console.log(response);
    }
  };

  const getMyTrips = async () => {
    const tripsUrl = `${process.env.REACT_APP_API_HOST}/trips/id/${userIdInt}`;
    const response = await fetch(tripsUrl, {
      credentials: "include",
    });

    if (response.ok) {
      const data = await response.json();
      setMyTrips(data);
    }
  };

  useEffect(() => {
    if(userIdInt !== 0){
    getPlannerTripsData();
    getMyTrips();
    }
  }, [userIdInt]); //eslint-disable-line react-hooks/exhaustive-deps

  const handleProfilePicChange = (event) => {
    setProfilePic(event.target.value);
  };
  const handleSubmit = async (event) => {
    event.preventDefault();
    const data = {
      user_id: userIdInt,
      bio: bio,
      profile_pic: profile_pic,
    };

    const updateUserProfileUrl = `${process.env.REACT_APP_API_HOST}/users/${userIdInt}`;
    await fetch(updateUserProfileUrl, {
      method: "PUT",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
  };

  const filteredTrips = plannerTrips.filter((trip) =>
    trip.planner.includes(trip_query)
  );

  return (
    <>
      <div className="my-3 d-flex">
        <div
          className="shadow p-4 mt-4 container"
          style={{ width: "225px", height: "250px", display: "inline-block" }}
        >
          <input
            type="text"
            placeholder="Enter profile pic url"
            value={profile_pic}
            onChange={handleProfilePicChange}
          />
          {profile_pic && (
            <img src={profile_pic} className="img-thumbnail img" alt="" />
          )}
        </div>
      </div>
      <div className="my-3 d-flex">
        <div className="container">
          <div className="row">
            <div className="shadow p-4 mt-4" style={{ height: "250px" }}>
              <form onSubmit={(event) => handleSubmit(event)} id="bio">
                <div className="form-floating mb-3">
                  <textarea
                    style={{ height: "200px" }}
                    value={bio}
                    placeholder="Tell us about you!"
                    onChange={(event) => {
                      setBio(event.target.value);
                    }}
                    className="form-control"
                    name="bio"
                  />
                  <label htmlFor="bio">Tell us about you!</label>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
      <button className="btn btn-primary btn-sm m-1" onClick={handleSubmit}>
        Save Changes
      </button>
      <div>
        <button
          className="btn btn-info btn-sm m-1"
          onClick={() => navigate("/friends")}
        >
          Add Friends
        </button>
      </div>
      <h1>Trips I'm Planning</h1>
      <div>
        <label
          className="form-control my-sm-0"
          type="text"
          placeholder="Trip History"
          onChange={(e) => setTripQuery(e.target.value)}
        />
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Trip Name</th>
              <th>City</th>
              <th>Country</th>
              <th>Start Date</th>
              <th>End Date</th>
            </tr>
          </thead>
          <tbody>
            {filteredTrips.map((filteredTrips) => {
              return (
                <tr key={filteredTrips.trip_id}>
                  <td>
                    <Link to={`/trips/${filteredTrips.trip_id}`}>
                      {filteredTrips.trip_name}
                    </Link>
                  </td>
                  <td>{filteredTrips.city}</td>
                  <td>{filteredTrips.country}</td>
                  <td>{filteredTrips.start_date}</td>
                  <td>{filteredTrips.end_date}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
        <div>
          <button
            className="btn btn-primary btn-sm m-1"
            onClick={() => navigate("/trips")}
          >
            Create a Trip
          </button>
        </div>
        <div>
          <h1>Trips I'm Going On</h1>
          <table className="table table-striped">
            <thead>
              <tr>
                <th>Trip</th>
                <th>City</th>
                <th>Country</th>
                <th>Start Date</th>
                <th>End Date</th>
                <th>Planner</th>
              </tr>
            </thead>
            <tbody>
              {myTrips.map((trip) => {
                return (
                  <tr key={trip.trip_id} value={trip.trip_name}>
                    <td>
                      <Link to={`/trips/${trip.trip_id}`}>
                        {trip.trip_name}
                      </Link>
                    </td>
                    <td>{trip.city}</td>
                    <td>{trip.country}</td>
                    <td>{trip.start_date}</td>
                    <td>{trip.end_date}</td>
                    <td>{trip.planner}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </>
  );
};

export default UserProfileForm;

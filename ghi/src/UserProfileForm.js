import { useState, useEffect } from "react";
import useToken from "@galvanize-inc/jwtdown-for-react";
import { Link } from "react-router-dom";

const UserProfileForm = () => {
  const [userIdInt, setUserIdInt] = useState(0);
  const [bio, setBio] = useState("");
  const [profile_pic, setProfilePic] = useState("");
  const [trips, setTrips] = useState([]);
  const [trip_query, setTripQuery] = useState("");
  const { token } = useToken();

  const getTripsData = async () => {
    const tripUrl = `${process.env.REACT_APP_API_HOST}/trips`;
    const response = await fetch(tripUrl, {
      credentials: "include",
    });

    if (response.ok) {
      const tripsData = await response.json();
      setTrips(tripsData);
    } else {
      console.log(response);
    }
  };

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
    getTripsData();
    getUserData();
  }, [token]); //eslint-disable-line react-hooks/exhaustive-deps

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

  const filteredTrips = trips.filter((trip) =>
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
      <button className="btn btn-primary" onClick={handleSubmit}>
        Save Changes
      </button>
      <h1>Trip History</h1>
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
              <th>Trip ID</th>
              <th>Planner</th>
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
                  <td>{filteredTrips.trip_id}</td>
                  <td>{filteredTrips.planner}</td>
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
      </div>
    </>
  );
};

export default UserProfileForm;

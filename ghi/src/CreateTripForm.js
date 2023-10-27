import { useState, useEffect } from "react";
import React from "react";
import { useNavigate } from "react-router-dom";

function CreateTrip() {
  const [countries, setCountries] = useState([]);
  const [tripName, setTripName] = useState("");
  const [city, setCity] = useState("");
  const [country, setCountry] = useState("");
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");

  const getCountries = async () => {
    const countriesUrl = `${process.env.REACT_APP_API_HOST}/countries`;
    const response = await fetch(countriesUrl, { credentials: "include" });
    if (response.ok) {
      const data = await response.json();
      setCountries(data);
    }
  };

  const navigate = useNavigate();

  const handleSubmit = async (event) => {
    event.preventDefault();

    const data = {};

    data.trip_name = tripName;
    data.city = city;
    data.country = country;
    data.start_date = startDate;
    data.end_date = endDate;


    const tripUrl = `${process.env.REACT_APP_API_HOST}/trips`;
    const fetchOptions = {
      method: "post",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include",
    };

    navigate('/profile');

    const tripResponse = await fetch(tripUrl, fetchOptions);
    if (tripResponse.ok) {
      setTripName("");
      setCity("");
      setCountry("");
      setStartDate("");
      setEndDate("");
    }
  };

  useEffect(() => {
    getCountries();
  }, []); //eslint-disable-line react-hooks/exhaustive-deps

  return (
    <div className="row">
      <div className="offset-3 col-6">
        <div className="shadow p-4 mt-4">
          <h1>Create a New Adventure</h1>
          <form onSubmit={handleSubmit} id="create-conference-form">
            <div className="form-floating mb-3">
              <input
                value={tripName}
                onChange={(e) => setTripName(e.target.value)}
                placeholder="Trip Name"
                required
                type="text"
                id="trip_name"
                name="trip_name"
                className="form-control"
              />
              <label htmlFor="trip_name">Trip Name</label>
            </div>
            <div className="form-floating mb-3">
              <input
                value={city}
                onChange={(e) => setCity(e.target.value)}
                placeholder="City"
                required
                type="text"
                id="city"
                name="city"
                className="form-control"
              />
              <label htmlFor="city">City</label>
            </div>
            <div className="mb-3">
              <label htmlFor="country" className="form-label">
                Country
              </label>
              <select
                value={country}
                onChange={(e) => setCountry(e.target.value)}
                required
                id="country"
                name="country"
                className="form-select"
              >
                <option value="">Choose a Country</option>
                {countries.map((country) => {
                  return (
                    <option value={country.country_id} key={country.country_id}>
                      {country.country_name}
                    </option>
                  );
                })}
              </select>
            </div>
            <div className="form-floating mb-3">
              <input
                value={startDate}
                onChange={(e) => setStartDate(e.target.value)}
                placeholder="Start Date"
                required
                type="text"
                id="start_date"
                name="start_date"
                className="form-control"
              />
              <label htmlFor="start_date">Start Date</label>
            </div>
            <div className="form-floating mb-3">
              <input
                value={endDate}
                onChange={(e) => setEndDate(e.target.value)}
                placeholder="End Date"
                required
                type="text"
                id="end_date"
                name="end_date"
                className="form-control"
              />
              <label htmlFor="end_date">End Date</label>
            </div>
            <button className="btn btn-primary">Create</button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default CreateTrip;

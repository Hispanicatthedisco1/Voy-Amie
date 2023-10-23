import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

function TripsFinalized() {
    const [activities, setActivities] = useState([]);
    const [query, setQuery] = useState("");
    let { trip_id } = useParams();
    let trip_id_int = parseInt(trip_id)

    const filteredDate = activities.filter(activity => activity.date.includes(query))

    const getActivitiesData = async () => {
        const url = `${process.env.REACT_APP_API_HOST}/activities/`;
        const response = await fetch(url, {
            credentials: "include",
        });

        if (response.ok) {
            const data = await response.json();
            setActivities(data);
        } else {
            console.log(response);
        }
    }

    useEffect(() => {
        getActivitiesData();
    }, []);

    return (
        <>
            <h1>Trip Itinerary</h1>
            <div>
                <input className="form-control my-sm-0" type="search" placeholder="Search by Date" onChange={(e) => setQuery(e.target.value)}/>
                <table className='table table-dark table-striped'>
                    <thead>
                        <tr>
                            <th>Trip Activity</th>
                            <th>Title</th>
                            <th>URL</th>
                            <th>Date</th>
                            <th>Time</th>
                            <th>Vote</th>
                        </tr>
                    </thead>
                    <tbody>
                            {filteredDate.map((filteredDate) => {
                                if (trip_id_int === filteredDate.trip && filteredDate.status === "finalized") {
                                return (
                                    <tr key={filteredDate.activity_id}>
                                        <td>{filteredDate.activity_id}</td>
                                        <td>{filteredDate.title}</td>
                                        <td>{filteredDate.url}</td>
                                        <td>{filteredDate.date}</td>
                                        <td>{filteredDate.time}</td>
                                        <td>{filteredDate.vote}</td>
                                    </tr>
                                );
                                } else {
                                    return null
                                }
                            })}
                            return null;
                    </tbody>
                </table>
            </div>
        </>
    );
}

export default TripsFinalized;

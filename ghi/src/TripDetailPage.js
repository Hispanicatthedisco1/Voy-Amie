import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { Link, useNavigate } from "react-router-dom";

function TripDetail() {
  let params = useParams();
  let paramsInt = parseInt(params.trip_id);
  const [activities, setActivities] = useState([]);
  const [formData, setFormData] = useState({
    title: "",
    url: "",
    date: "",
    time: "",
  });
  const [comments, setComments] = useState([]);
  const [formCommentData, setFormCommentData] = useState({
    comment: "",
  });
  const [participants, setParticipants] = useState([]);
  const [user, setUser] = useState([]);
  const [votes, setVotes] = useState([]);
  const [trip, setTrip] = useState([]);
  const navigate = useNavigate();

  function countParticipants(participants) {
    let count = 1;
    for (let i = 0; i < participants.length; i++) {
      if (participants[i]["trip_id"] === paramsInt) {
        count += 1;
      }
    }
    return count;
  }

  const getVotesData = async () => {
    const votesURL = `${process.env.REACT_APP_API_HOST}/votes`;
    const response = await fetch(votesURL, {
      credentials: "include",
    });
    if (response.ok) {
      const data = await response.json();
      setVotes(data);
    }
  };

  const getActivitiesData = async () => {
    const activitiesUrl = `${process.env.REACT_APP_API_HOST}/activities`;
    const response = await fetch(activitiesUrl, {
      credentials: "include",
    });
    if (response.ok) {
      const data = await response.json();
      // console.log(data);
      setActivities(data);
    }
  };

  // console.log(votes);

  const getCommentsData = async () => {
    const commentsUrl = `${process.env.REACT_APP_API_HOST}/comments?trip=${paramsInt}`;
    const response = await fetch(commentsUrl, {
      credentials: "include",
    });
    if (response.ok) {
      const commentsData = await response.json();
      // console.log(commentsData);
      setComments(commentsData);
    }
  };

  const getParticipantsData = async () => {
    const participantsUrl = `${process.env.REACT_APP_API_HOST}/trips/${paramsInt}/participants`;
    const response = await fetch(participantsUrl, {
      credentials: "include",
    });
    if (response.ok) {
      const participantsData = await response.json();
      setParticipants(participantsData);
    }
  };

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

  const fetchTripData = async () => {
    const tripURL = `${process.env.REACT_APP_API_HOST}/trips/${paramsInt}`;
    const response = await fetch(tripURL, { credentials: "include" });
    if (response.ok) {
      const data = await response.json();
      setTrip(data);
    }
  };

  const handleUpvote = async (
    activity_id,
    title,
    url,
    date,
    time,
    status,
    vote
  ) => {
    await fetch(`${process.env.REACT_APP_API_HOST}/activities/${activity_id}`, {
      method: "PUT",
      body: JSON.stringify({
        trip: paramsInt,
        title: title,
        url: url,
        date: date,
        time: time,
        status: status,
        vote: vote + 1,
      }),
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
      },
    });
    getParticipantsData();
    countParticipants(participants);

    await fetch(`${process.env.REACT_APP_API_HOST}/votes`, {
      method: "POST",
      body: JSON.stringify({
        vote_id: user.user.user_id,
        activity_id: activity_id,
      }),
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
      },
    });

    getActivitiesData();
    getVotesData();

    const partCount = countParticipants(participants);
    const upVoted = vote + 1;

    if (upVoted >= Math.floor(partCount / 2)) {
      await fetch(
        `${process.env.REACT_APP_API_HOST}/activities/${activity_id}`,
        {
          method: "PUT",
          body: JSON.stringify({
            trip: paramsInt,
            title: title,
            url: url,
            date: date,
            time: time,
            status: "FINALIZED",
            vote: upVoted,
          }),
          credentials: "include",
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
    }
    getActivitiesData();
    countParticipants(participants);
  };
  const handleDownvote = async (
    activity_id,
    title,
    url,
    date,
    time,
    status,
    vote
  ) => {
    await fetch(`${process.env.REACT_APP_API_HOST}/activities/${activity_id}`, {
      method: "PUT",
      body: JSON.stringify({
        trip: paramsInt,
        title: title,
        url: url,
        date: date,
        time: time,
        status: status,
        vote: vote - 1,
      }),
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
      },
    });

    getParticipantsData();
    countParticipants(participants);

    await fetch(`${process.env.REACT_APP_API_HOST}/votes`, {
      method: "POST",
      body: JSON.stringify({
        vote_id: user.user.user_id,
        activity_id: activity_id,
      }),
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
      },
    });

    getActivitiesData();
    getVotesData();
    countParticipants(participants);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const activityURL = `${process.env.REACT_APP_API_HOST}/activity`;
    const fetchConfig = {
      method: "post",
      body: JSON.stringify(
        formData,
        (formData["status"] = "PENDING"),
        (formData["vote"] = 0),
        (formData["trip"] = paramsInt)
      ),
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
      },
    };

    const response = await fetch(activityURL, fetchConfig);
    if (response.ok) {
      await response.json();

      setFormData({
        title: "",
        url: "",
        date: "",
        time: "",
      });
    }
    getActivitiesData();
  };

  const handleFormChange = (e) => {
    const value = e.target.value;
    const inputName = e.target.name;
    setFormData({
      ...formData,

      [inputName]: value,
    });
  };

  const handleCommentSubmit = async (e) => {
    e.preventDefault();

    const commentURL = `${process.env.REACT_APP_API_HOST}/comments`;
    const fetchConfig = {
      method: "post",
      body: JSON.stringify(
        formCommentData,
        (formCommentData["trip"] = paramsInt)
      ),
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
      },
    };

    const response = await fetch(commentURL, fetchConfig);
    if (response.ok) {
      await response.json();

      setFormCommentData({
        comment: "",
      });
    }
    getCommentsData();
  };

  const handleCommentFormChange = (e) => {
    const value = e.target.value;
    const inputName = e.target.name;
    setFormCommentData({
      ...formCommentData,

      [inputName]: value,
    });
  };

  const isPlanner = () => {
    if (user?.user?.username === trip.planner) {
      return true;
    } else {
      return false;
    }
  };

  useEffect(() => {
    getActivitiesData();
    getCommentsData();
    getParticipantsData();
    getLoggedInUserData();
    getVotesData();
    fetchTripData();
    isPlanner();
    countParticipants(participants);
  }, []); //eslint-disable-line react-hooks/exhaustive-deps

  const isParticipant = participants.some(
    (participants) => participants?.user_id === user?.user?.user_id
  );
  if (!(isParticipant || isPlanner())) {
    return <p>You are not the Planner or a Participant</p>;
  }

  return (
    <>
      <h1 className="text-center m-3">{trip?.trip_name}</h1>
      <Link to={`/finalized/${paramsInt}`}>
        <button
          className="btn btn btn-sm m-2"
          style={{
            position: "fixed",
            right: "0px",
            backgroundColor: "#0077b6",
            color: "white",
          }}
        >
          TripsFinalized
        </button>
      </Link>
      <h2>Participants</h2>

      {participants.map((participant) => {
        return (
          <p
            key={participant.participant_id}
            value={participant.username}
            className="d-inline-block mx-4"
          >
            {participant.username}
          </p>
        );
      })}
      {isPlanner() ? (
        <div>
          <button
            className="btn btn-info btn-sm m-1"
            onClick={() => navigate(`/trips/${paramsInt}/participants`)}
          >
            Add Participants
          </button>
        </div>
      ) : null}
      <div>
        <h2 className="mb-3">Activities</h2>
        {activities.map((activities) => {
          if (
            paramsInt === activities.trip &&
            activities.status === "PENDING"
          ) {
            return (
              <div
                className="accordion mb-2"
                id="accordionExample"
                key={activities.activity_id}
              >
                <div className="accordion-item">
                  <h2 className="accordion-header">
                    <button
                      className="accordion-button collapsed"
                      type="button"
                      data-bs-toggle="collapse"
                      data-bs-target={`#collapseTwo${activities.activity_id}`}
                      aria-expanded="false"
                      aria-controls="collapseTwo"
                      style={{ opacity: 0.5 }}
                    >
                      {activities.title}
                    </button>
                  </h2>
                  <div
                    id={`collapseTwo${activities.activity_id}`}
                    className="accordion-collapse collapse"
                    data-bs-parent="#accordionExample"
                  >
                    <div className="accordion-body">
                      <p>Status: {activities.status}</p>
                      <p>Date: {activities.date}</p>
                      <p>Time: {activities.time}</p>
                      <p>
                        Link:
                        <Link to={activities.url}>{activities.title}</Link>
                      </p>
                      <p>Vote: {activities.vote}</p>
                      <span>
                        {votes.includes(activities.activity_id) ? null : (
                          <>
                            <button
                              className="btn btn p-2 m-2 rounded-circle btn-sm"
                              style={{ backgroundColor: "#16f796" }}
                              onClick={() =>
                                handleUpvote(
                                  activities.activity_id,
                                  activities.title,
                                  activities.url,
                                  activities.date,
                                  activities.time,
                                  activities.status,
                                  activities.vote
                                )
                              }
                            >
                              <svg
                                xmlns="http://www.w3.org/2000/svg"
                                width="16"
                                height="16"
                                fill="currentColor"
                                className="bi bi-arrow-up"
                                viewBox="0 0 16 16"
                              >
                                <path
                                  fillRule="evenodd"
                                  d="M8 15a.5.5 0 0 0 .5-.5V2.707l3.146 3.147a.5.5 0 0 0 .708-.708l-4-4a.5.5 0 0 0-.708 0l-4 4a.5.5 0 1 0 .708.708L7.5 2.707V14.5a.5.5 0 0 0 .5.5z"
                                />
                              </svg>
                            </button>
                            <button
                              className="btn btn p-2 rounded-circle btn-sm"
                              style={{ backgroundColor: "#f5182f" }}
                              onClick={() =>
                                handleDownvote(
                                  activities.activity_id,
                                  activities.title,
                                  activities.url,
                                  activities.date,
                                  activities.time,
                                  activities.status,
                                  activities.vote
                                )
                              }
                            >
                              <svg
                                xmlns="http://www.w3.org/2000/svg"
                                width="16"
                                height="16"
                                fill="currentColor"
                                className="bi bi-arrow-down"
                                viewBox="0 0 16 16"
                              >
                                <path
                                  fillRule="evenodd"
                                  d="M8 1a.5.5 0 0 1 .5.5v11.793l3.146-3.147a.5.5 0 0 1 .708.708l-4 4a.5.5 0 0 1-.708 0l-4-4a.5.5 0 0 1 .708-.708L7.5 13.293V1.5A.5.5 0 0 1 8 1z"
                                />
                              </svg>
                            </button>
                          </>
                        )}
                      </span>
                    </div>
                  </div>
                </div>
              </div>
            );
          } else {
            return null;
          }
        })}
      </div>
      <button
        type="button"
        className="btn btn-primary"
        data-bs-toggle="modal"
        data-bs-target="#staticBackdrop"
        style={{ backgroundColor: "#0096c7" }}
      >
        Add Activity
      </button>
      <div
        className="modal fade"
        id="staticBackdrop"
        data-bs-backdrop="static"
        data-bs-keyboard="false"
        tabIndex="-1"
        aria-labelledby="staticBackdropLabel"
        aria-hidden="true"
      >
        <div className="modal-dialog">
          <div className="modal-content">
            <div className="modal-header">
              <h1
                className="modal-title fs-5 text-center"
                id="staticBackdropLabel"
              >
                Add An Activity
              </h1>
              <button
                type="button"
                className="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              ></button>
            </div>
            <form onSubmit={handleSubmit} id="create-customer-form">
              <div className="modal-body">
                <label htmlFor="title">Title</label>
                <input
                  value={formData.title}
                  onChange={handleFormChange}
                  placeholder="Title"
                  required
                  type="text"
                  id="title"
                  name="title"
                  className="form-control mb-2"
                />

                <label htmlFor="url">URL</label>
                <input
                  value={formData.url}
                  onChange={handleFormChange}
                  placeholder="URL"
                  required
                  type="text"
                  id="url"
                  name="url"
                  className="form-control mb-2"
                />

                <label htmlFor="date">Date</label>
                <input
                  value={formData.date}
                  onChange={handleFormChange}
                  placeholder="Date"
                  required
                  type="text"
                  id="date"
                  name="date"
                  className="form-control mb-2"
                />

                <label htmlFor="">Time</label>
                <input
                  value={formData.time}
                  onChange={handleFormChange}
                  placeholder="Time"
                  required
                  type="text"
                  id="time"
                  name="time"
                  className="form-control"
                />
              </div>
              <div className="modal-footer">
                <button
                  type="submit"
                  className="btn btn-primary"
                  data-bs-dismiss="modal"
                >
                  Create
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>

      <div>
        <h2 className="my-3">Comments</h2>
        {comments.map((comments) => {
          return (
            <div
              className="accordion mb-2"
              id="accordionExample"
              key={comments.comment_id}
            >
              <div className="accordion-item">
                <h2 className="accordion-header">
                  <button
                    className="accordion-button collapsed"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target={`#collapseTwo${comments.comment_id}`}
                    aria-expanded="false"
                    aria-controls="collapseTwo"
                  >
                    {comments.commenter}
                  </button>
                </h2>
                <div
                  id={`collapseTwo${comments.comment_id}`}
                  className="accordion-collapse collapse"
                  data-bs-parent="#accordionExample"
                >
                  <div className="accordion-body">
                    <p>{comments.comment}</p>
                  </div>
                </div>
              </div>
            </div>
          );
        })}
      </div>

      <button
        type="button"
        className="btn btn-primary"
        data-bs-toggle="modal"
        data-bs-target="#exampleModal"
        style={{ backgroundColor: "#0096c7" }}
      >
        Add Comment
      </button>

      <div
        className="modal fade"
        id="exampleModal"
        tabIndex="-1"
        aria-labelledby="exampleModalLabel"
        aria-hidden="true"
      >
        <div className="modal-dialog">
          <div className="modal-content">
            <div className="modal-header">
              <h1 className="modal-title fs-5" id="exampleModalLabel">
                Add A Comment
              </h1>
              <button
                type="button"
                className="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              ></button>
            </div>
            <form onSubmit={handleCommentSubmit} id="create-customer-form">
              <div className="modal-body">
                <label htmlFor="comment">Comment</label>
                <input
                  value={formCommentData.comment}
                  onChange={handleCommentFormChange}
                  placeholder="Comment"
                  required
                  type="text"
                  id="comment"
                  name="comment"
                  className="form-control"
                />
              </div>
              <div className="modal-footer">
                <button
                  type="submit"
                  className="btn btn-primary"
                  data-bs-dismiss="modal"
                >
                  Create
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </>
  );
}

export default TripDetail;

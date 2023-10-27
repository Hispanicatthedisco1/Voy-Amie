import { useState, useEffect } from "react";
import React from "react";

function CreateFriend() {
  const [users, setUsers] = useState([]);
  const [friends, setFriends] = useState([]);
  const [query, setQuery] = useState("");

  const fetchAllUsers = async () => {
    const usersURL = `${process.env.REACT_APP_API_HOST}/users`;
    const response = await fetch(usersURL, { credentials: "include" });
    if (response.ok) {
      const data = await response.json();
      setUsers(data);
    }
  };

  const fetchFriends = async () => {
    const usersURL = `${process.env.REACT_APP_API_HOST}/friends`;
    const response = await fetch(usersURL, { credentials: "include" });
    if (response.ok) {
      const data = await response.json();
      setFriends(data);
    }
  };

  const handleSubmit = async (user2Id) => {
    const data = {};
    data.user2_id = user2Id;

    const createFriendUrl = `${process.env.REACT_APP_API_HOST}/friends`;
    const fetchConfig = {
      method: "POST",
      body: JSON.stringify(data),
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
      },
    };
    const friendshipResponse = await fetch(createFriendUrl, fetchConfig);
    if (friendshipResponse.ok) {
      fetchAllUsers();
      fetchFriends();
    }
  };

  let alreadyFriends = [];
  for (let friend of friends) {
    alreadyFriends.push(friend.user_id);
  }

  const filteredUsers = users.filter((user) =>
    user.username.toLowerCase().includes(query.toLowerCase())
  );

  useEffect(() => {
    fetchAllUsers();
    fetchFriends();
  }, []); //eslint-disable-line react-hooks/exhaustive-deps

  return (
    <>
      <div>
        <input
          className="form-control my-sm-0"
          type="search"
          placeholder="Type your future friend's username!"
          onChange={(e) => setQuery(e.target.value)}
        />
      </div>
      <div className="d-flex flex-column m-2">
        {query.length > 0 &&
          filteredUsers.map((user) => {
            const isFriend = alreadyFriends.includes(user.user_id);
            if (isFriend === false) {
              return (
                <span
                  className="d-inline-flex m-2"
                  key={user.user_id}
                  value={user.username}
                >
                  <p className="px-1">{user.username}</p>
                  <button
                    className="btn btn-info btn-sm m-1"
                    onClick={() => handleSubmit(user.user_id)}
                  >
                    Add Friend
                  </button>
                </span>
              );
            } else{
              return(null)
            }
          })}
      </div>
    </>
  );
}

export default CreateFriend;

import { useState, useEffect } from "react";
import React from 'react'
import { useParams } from "react-router-dom";
import { useNavigate } from "react-router-dom";


function CreateParticipants(){
    let params = useParams();
    let paramsInt = parseInt(params.trip_id);
    const [friends, setFriends] = useState([]);
    const [participants, setParticipants] = useState([]);
    const navigate = useNavigate();


    const fetchFriends = async () => {
        const friendsUrl = `${process.env.REACT_APP_API_HOST}/friends`
        const response = await fetch (
            friendsUrl,
            {credentials: "include",}
        );
        if(response.ok){
            const data = await response.json();
            setFriends(data);
        };
    };

    const fetchParticipants = async () => {
        const participantsUrl = `${process.env.REACT_APP_API_HOST}/trips/${paramsInt}/participants`
        const response = await fetch (
            participantsUrl,
            {credentials: "include",}
        );
        if(response.ok){
            const data = await response.json();
            setParticipants(data);
        }
    };

    const makeParticipant = async (userId) => {
        const data = {};
        data.user_id = userId;
        data.trip_id = paramsInt;

        const participantURL = `${process.env.REACT_APP_API_HOST}/participants`
        const fetchConfig = {
            method: "POST",
            body: JSON.stringify(data),
            credentials: "include",
            headers: {
                'Content-Type': 'application/json',
            },
        };
        const participantResponse = await fetch(participantURL, fetchConfig);
        if (participantResponse.ok){
            fetchParticipants();
        };
    };

    const removeParticipant = async (id) => {
        const data = {};
        data.participant_id = id

        const deleteParticipantUrl = `${process.env.REACT_APP_API_HOST}/participants/${id}`;
        const fetchConfig = {
            method: "DELETE",
            body: JSON.stringify(data),
            credentials: "include",
            headers: {
                'Content-Type': 'application/json',
            },
        };
        const delResponse = await fetch(deleteParticipantUrl, fetchConfig)
        if(delResponse.ok){
            fetchParticipants();
        };
    };


    useEffect(() => {
        fetchFriends();
        fetchParticipants();
     }, []); //eslint-disable-line react-hooks/exhaustive-deps


    return(
        <>
            <h1>Add Companions to Your Trip!</h1>
            <div>
                <table className="table table-striped">
                    <thead>
                        <tr>
                            <th>Friend</th>
                            <th>Add to Trip</th>
                        </tr>
                    </thead>
                    <tbody>
                        {friends.map((friend) => {
                            const isParticipant = participants.some((participant) => (participant.user_id === friend.user_id) )
                            if(!isParticipant){
                            return(
                                <tr key={friend.user_id} value={friend.user_id}>
                                    <td>{friend.username}</td>
                                    <td>
                                        <button className="btn btn-success" onClick={() => makeParticipant(friend.user_id)}>Add</button>
                                    </td>
                                </tr>
                            )}else{
                                return null
                            }
                        })}
                    </tbody>
                </table>
            </div>
            <div>
                <table className="table table-striped">
                    <thead>
                        <tr>
                            <th>Trip Participants</th>
                            <th>Remove</th>
                        </tr>
                    </thead>
                    <tbody>
                        {participants.map((participant) => {
                            return(
                                <tr key={participant.participant_id}>
                                    <td>{participant.username}</td>
                                    <td>
                                        <button className="btn btn-danger" onClick={() => removeParticipant(participant.participant_id)}>Remove</button>
                                    </td>
                                </tr>
                            );
                        })}
                    </tbody>
                    </table>
                <button className="btn btn-info" onClick={ () => navigate(`/trips/${paramsInt}`)}>Back to Trip</button>
            </div>
        </>
    );
};

export default CreateParticipants;

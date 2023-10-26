import { useState } from "react";
import useToken from "@galvanize-inc/jwtdown-for-react";
import { useNavigate } from "react-router-dom";

const SignUpForm = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [bio, setBio] = useState("");
  const [profile_pic, setProfilePic] = useState("");
  const { register } = useToken();
  const navigate = useNavigate();

  const handleRegistration = async (e) => {
    e.preventDefault();
    const accountData = {
      username: username,
      password: password,
      email: email,
      bio: bio,
      profile_pic: profile_pic,
    };

    const registrationResponse = await register(
      accountData,
      `${process.env.REACT_APP_API_HOST}/users`
    );

    if (registrationResponse && registrationResponse.ok) {
      const user_id = registrationResponse.data.user_id;

      const profileData = {
        bio,
        profile_pic,
      };

      const profileUrl = `${process.env.REACT_APP_API_HOST}/users/${user_id}`;
      const fetchConfig = {
        method: "POST",
        body: JSON.stringify(profileData),
        credentials: "include",
        headers: {
          "Content-Type": "application/json",
        },
      };

      const response = await fetch(profileUrl, fetchConfig);
      if (response.ok) {
        setBio("");
        setProfilePic("");
      }

      e.target.reset();
      navigate("/profile/user_id");
    }
  };

  return (
    <div className="card text-bg-light mb-3">
      <h5 className="card-header">Signup</h5>
      <div className="card-body">
        <form onSubmit={(e) => handleRegistration(e)}>
          <div className="mb-3">
            <label className="form-label">username</label>
            <input
              name="username"
              type="text"
              className="form-control"
              onChange={(e) => {
                setUsername(e.target.value);
              }}
            />
          </div>
          <div className="mb-3">
            <label className="form-label">password</label>
            <input
              name="password"
              type="password"
              className="form-control"
              onChange={(e) => {
                setPassword(e.target.value);
              }}
            />
          </div>
          <div className="mb-3">
            <label className="form-label">email</label>
            <input
              name="email"
              type="text"
              className="form-control"
              onChange={(e) => {
                setEmail(e.target.value);
              }}
            />
          </div>
          <div className="mb-3">
            <label className="form-label">bio</label>
            <input
              name="bio"
              type="text"
              className="form-control"
              onChange={(e) => {
                setBio(e.target.value);
              }}
            />
          </div>
          <div className="mb-3">
            <label className="form-label">Profile Pic</label>
            <input
              name="profile_pic"
              type="text"
              className="form-control"
              onChange={(e) => {
                setProfilePic(e.target.value);
              }}
            />
          </div>
          <div>
            <input className="btn btn-primary" type="submit" value="Register" />
          </div>
        </form>
      </div>
    </div>
  );
};

export default SignUpForm;

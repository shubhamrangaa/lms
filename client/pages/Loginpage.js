import React, { useState } from "react";
import LoginForm from "../components/LoginForm";
import Navbar from "../components/Navbar";

const Loginpage = () => {
  const adminUser = {
    email: "prachi@gmail.com",
    password: "1234",
  };
  const [user, setUser] = useState({ name: "", email: "" });
  const [error, setError] = useState("");

  const Login = (details) => {
    console.log(details);
  };

  const Logout = () => {
    console.log("Logout");
  };
  return (
    <div className={user.email != ""}>
      <Navbar />

      <LoginForm login={Login} error={error} />
    </div>
  );
};

export default Loginpage;

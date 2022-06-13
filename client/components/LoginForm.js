import React, { useState } from "react";
import styles from "../styles/login.module.css";

const LoginForm = ({ Login, error }) => {
  const [details, setDetails] = useState({ name: "", email: "", password: "" });
  const submitHandler = (e) => {
    e.preeventDefault();
    Login(details);
  };
  return (
    <form onSubmit={submitHandler}>
      <div className={styles.formContainer}>
        <div className="form-inner">
          <h1>Welcome!!</h1>
          <h6>Sign in to post your thoughts</h6>
          <div className="form-group">
            <input type="email" id="email" placeholder="Enter your email" />
          </div>
          <div className="form-group">
            <input type="text" id="password" placeholder="Enter password" />
          </div>
          <input type="submit" value="Log In" />
        </div>
      </div>
    </form>
  );
};

export default LoginForm;

import styles from "../styles/navbar.module.css";
import { useState } from "react";
const Navbar = () => {
  const [click, setClick] = useState(false);
  const handleClick = () => setClick(!click);
  const closeMobileMenu = () => setClick(false);
  return (
    <div className={styles.header}>
      <navbar className={styles.navContainer}>
        <div className={styles.navItemsWrapper}>
          <div className={styles.navItem}>
            {/* <a href="#">nuntium</a> */}
            <ul>
              <li className={styles.option} onClick={closeMobileMenu}>
                <a href="#">BLOGS</a>
              </li>
              <li className={styles.option} onClick={closeMobileMenu}>
                <a href="#">Home</a>
              </li>
              <li className={styles.option} onClick={closeMobileMenu}>
                <a href="#">Tags</a>
              </li>
              <li className={styles.option} onClick={closeMobileMenu}>
                <a href="#">About</a>
              </li>
            </ul>
          </div>
          <div>
            <a className={styles.buttonLogin} href="#">
              Login
            </a>
          </div>
        </div>
      </navbar>
    </div>
  );
};

export default Navbar;

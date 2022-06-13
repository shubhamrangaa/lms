import styles from "../styles/hero.module.css";
import Image from "next/image";

const Hero = () => {
  return (
    <div>
      <div className={styles.heroContainer}>
        <div className={styles.heroWrapper}>
          <div className={styles.contentContainer}>
            <h6>Featured Article</h6>
            <h1>World’s Most Dangerous Technology Ever Made.</h1>
            <span>
              <p>
                Proident aliquip velit qui commodo officia qui consectetur dolor
                ullamco aliquip elit incididunt. Ea minim ex consectetur
                excepteur. Ex laborum nostrud mollit sint consectetur Lorem amet
                aliqua do enim. Commodo duis dolor anim excepteur. In aliquip
                mollit nulla consequat velit magna.
              </p>
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Hero;

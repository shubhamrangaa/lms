import styles from "../styles/display.module.css";
import Image from "next/image";
import Link from "next/link";

const articleData = [
  {
    name: "Minimalism",
    description:
      "lorem ipsidslkfjoaifj sdofeo iwfjsv wiof ovfjks adfoiwnivo sdnvkfndefoisdahdvvwjf",
    imageUrl: "/static/Pic1.png",
  },
  {
    name: "Technology",
    description:
      "lorem ipsidslkfjoaifj sdofeo iwfjsv wiof ovfjks adfoiwnivo sdnvkfndefoisdahdvvwjf",
    imageUrl: "/static/Pic2.png",
  },
  {
    name: "Politics",
    description:
      "lorem ipsidslkfjoaifj sdofeo iwfjsv wiof ovfjks adfoiwnivo sdnvkfndefoisdahdvvwjf",
    imageUrl: "/static/Pic3.png",
  },
];

const Display = () => {
  return (
    <Link href="/article">
      <div className={styles.articleContainer}>
        {/* <div className={styles.articleWrapper}> */}
        <h1>Recently Added </h1>
        <h1>______________________</h1>
        {articleData.map((article, index) => (
          <div className={styles.contentContainer} key={index}>
            <div className={styles.imageContainer}>
              <Image src={article.imageUrl} width={300} height={300}></Image>
            </div>
            <div className="styles.textContainer">
              <h1>{article.name}</h1>
              <p>{article.description}</p>
            </div>
          </div>
        ))}
      </div>
    </Link>
  );
};

export default Display;

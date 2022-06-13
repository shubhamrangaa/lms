import React from "react";
import styles from "../styles/article.module.css";
import Image from "next/image";
import Navbar from "../components/Navbar";

const articleData = [
  {
    imageUrl: "/static/Pic1.png",
    name: "Minimalism",
    about: "Ralph Hawkings . May 7 2021",
    description:
      "lorem ipsidslkfjoaifj sdofeo iwfjsv wiof ovfjks adfoiwnivo sdnvkfndefoisdahdvvwjflorem ipsidslkfjoaifj sdofeo iwfjsv wiof ovfjks adfoiwnivo sdnvkfndefoisdahdvvwjflorem ipsidslkfjoaifj sdofeo iwfjsv wiof ovfjks adfoiwnivo sdnvkfndefoisdahdvvwjflorem ipsidslkfjoaifj sdofeo iwfjsv wiof ovfjks adfoiwnivo sdnvkfndefoisdahdvvwjflorem ipsidslkfjoaifj sdofeo iwfjsv wiof ovfjks adfoiwnivo sdnvkfndefoisdahdvvwjflorem ipsidslkfjoaifj sdofeo iwfjsv wiof ovfjks adfoiwnivo sdnvkfndefoisdahdvvwjflorem ipsidslkfjoaifj sdofeo iwfjsv wiof ovfjks adfoiwnivo sdnvkfndefoisdahdvvwjflorem ipsidslkfjoaifj sdofeo iwfjsv wiof ovfjks adfoiwnivo sdnvkfndefoisdahdvvwjflorem ipsidslkfjoaifj sdofeo iwfjsv wiof ovfjks adfoiwnivo sdnvkfndefoisdahdvvwjflorem ipsidslkfjoaifj sdofeo iwfjsv wiof ovfjks adfoiwnivo sdnvkfndefoisdahdvvwjf",
  },
];
const Article = () => {
  return (
    <div className={styles.articleContainer}>
      <Navbar />
      {articleData.map((article, index) => (
        <div className={styles.contentContainer} key={index}>
          <h1>{article.name}</h1>
          <h6>{article.about}</h6>
          <div className={styles.imageContainer}>
            <Image src={article.imageUrl} width={700} height={500}></Image>
          </div>
          <p>{article.description}</p>
        </div>
      ))}
    </div>
  );
};

export default Article;

import React from "react";
import { Link } from "react-router-dom";
import "./homepage.css";
import { FileUploader } from "../components/fileUploader";
import Cards from "../components/cards";

function Home() {
  
  return (
    <div className="content">
      <FileUploader />
      {/* <div>
        <Link to="/algorithms">
          <button className="homeAlgorithms">Algorithms</button>
        </Link>
      </div> */}
      <Cards />
    </div>
  );
};

export default Home;
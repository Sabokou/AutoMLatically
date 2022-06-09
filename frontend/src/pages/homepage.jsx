import React from "react";
import { Link } from "react-router-dom";
import "./homepage.css";
import { FileUploader } from "../components/fileUploader";


function Home() {
  
  return (
    <div className="content">
      <FileUploader />
      <div>
        <Link to="/algorithms">
          <button className="homeAlgorithms">Algorithms</button>
        </Link>
      </div>
    </div>
  );
};

export default Home;
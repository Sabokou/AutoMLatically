import React from "react";
import { Link } from "react-router-dom";
import "./homepage.css";
import Cards from "../components/cards";
import { FileUploader } from "../components/fileUploader";

function Home(props) {
  return (
    <div className="content">
      {/* <FileUploader setCsvColumns={props.setCsvColumns} setCsvRows={props.setCsvRows} /> */}
      {/* <div>
        <Link to="/algorithms">
          <button className="homeAlgorithms">Algorithms</button>
        </Link>
      </div> */}
      <Cards />
    </div>
  );
}

export default Home;

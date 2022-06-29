import React from "react";
import { Link } from "react-router-dom";
import "./homepage.css";
import { FileUploader } from "../components/fileUploader";
import Cards from "../components/cards";
import { useState } from "react";

function Home() {
  const [csvColumns, setCsvColumns] = useState()
  const [csvRows, setCsvRows] = useState()
  return (
    <div className="content">
      {/* This code with the column dropdown can be used for the gold label selection in a card */}
      {csvColumns && 
      <select>
        {csvColumns.map( (item) => {
          return <option value={item}>{item}</option>
        })}
      </select>
      }
      <FileUploader setCsvColumns={setCsvColumns} setCsvRows={setCsvRows}/>
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
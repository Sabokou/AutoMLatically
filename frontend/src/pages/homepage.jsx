import React from "react";
import { Link } from "react-router-dom";
import "./homepage.css";

function Home() {
  
  return (
    <div className="content">
      <div className="select">
        <button>Select dataset</button>
        <button>Start training</button>
      </div>

      <div>
        <Link to="/algorithms">
          <button className="homeAlgorithms">Algorithms</button>
        </Link>
      </div>
    </div>
  );
};

export default Home;
import React from 'react'
import './cards.css';
import axios from "axios";

export default function Cards() {
  return (
    <div className="cardLayout">
      <div className="cardContainer box1">
        <p className="cardContainer header1">Choose Gold Label in Dataset</p>
      </div>
      <div className="cardContainer box2">
        <div className="switchBox">
          <p className="switchHeader">Regression</p>

          <label class="switch">
            <input type="checkbox" />
            <span class="slider round"></span>
          </label>
        </div>
        <div className="switchBox">
          <p className="switchHeader">Classification</p>
          <label class="switch">
            <input type="checkbox" />
            <span class="slider round"></span>
          </label>
        </div>
      </div>
      <div className="cardContainer box3">
        <div className="switchBox3">
          <p className="cardContainer header3">Start Training</p>
          <button className="button">
            <span>Go!</span>
          </button>
        </div>
      </div>
      <div className="cardContainer box4"></div>
    </div>
  );
}

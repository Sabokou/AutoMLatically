import React from "react";
import "./cards.css";
import axios from "axios";
import CsvLoader from "./CsvLoader";
import { useState } from "react";
import Selector from "./selector";
import { FileUploader } from "./fileUploader";
import CsvPreview from "./CsvPreview";

export default function Cards(props) {
  const [click, setClick] = useState(true);
  const [csvColumns, setCsvColumns] = useState();
  const [csvRows, setCsvRows] = useState();

  return (
    <div className="cardLayout">
      <div className="cardContainer box1">
        <p className="cardContainer header1">Choose Dataset</p>
        <FileUploader setCsvColumns={setCsvColumns} setCsvRows={setCsvRows} />

        {
          // table that displays the csv content
          csvColumns && (
            <CsvPreview column_data={csvColumns} row_data={csvRows} />
          )
        }
      </div>
      <div className="cardContainer box12">
        <p className="cardContainer header1"> Gold Label Selection</p>
        <Selector csvColumns={csvColumns} csvRows={csvRows} />
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
          <button className="button" onSubmit={() => setClick(!click)}>
            <span>Go!</span>
          </button>
        </div>
      </div>
      <div className="cardContainer box4"></div>
    </div>
  );
}

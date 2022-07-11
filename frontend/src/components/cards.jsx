import React from "react";
import "./cards.css";
import axios from "axios";
import CsvLoader from "./CsvLoader";
import { useState } from "react";
import Selector from "./selector";
import { FileUploader } from "./fileUploader";
import CsvPreview from "./CsvPreview";
import ModelSelector from "./ModelSelector";
import RequestModels from "./RequestModels";

export default function Cards(props) {
  const [click, setClick] = useState(true);
  const [csvColumns, setCsvColumns] = useState();
  const [csvRows, setCsvRows] = useState();
  const [mlKind, setMlKind] = useState("classification")
  const [selectedModels, setSelectedModels] = useState([])
  // maps the state of the regression/classification switch to the respective string
  const mlKindMap = { true: "regression", false: "classification" }

  var availModels = RequestModels()

  // switch between the classification and regression model if the Switch is activated
  const switchMlKind = (event) => {
    let checked = event.target.checked
    console.log('checked', checked)
    let kind = mlKindMap[checked]
    // reset the previously selected models, since regression and classfication should not be trained at the same time
    setSelectedModels([])
    setMlKind(kind)
    console.log('selectedModels', selectedModels)
  }


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
          <p className="switchHeader">Classification</p>
          <label class="switch">
            <input type="checkbox" onClick={(e) => switchMlKind(e)} />
            <span class="slider round"></span>
          </label>
          <p className="switchHeader">Regression</p>
        </div>
        <ModelSelector availModels={availModels} modelKind={mlKind} selectedModels={selectedModels} setSelectedModels={setSelectedModels} />
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

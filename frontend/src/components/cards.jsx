import React from "react";
import "./cards.css";
import axios from "axios";
import CsvLoader from "./CsvLoader";
import { useState } from "react";
import Selector from "./LabelSelector";
import { FileUploader } from "./fileUploader";
import CsvPreview from "./CsvPreview";
import ModelSelector from "./ModelSelector";
import RequestModels from "./RequestModels";
import ModelDownloader from "./ModelDownloader";

export default function Cards(props) {
  const backendUrl = "http://localhost:8001"

  const [goldLabel, setGoldLabel] = useState();
  const [csvColumns, setCsvColumns] = useState();
  const [csvRows, setCsvRows] = useState();
  const [mlKind, setMlKind] = useState("classification")
  const [selectedModels, setSelectedModels] = useState([])
  // maps the state of the regression/classification switch to the respective string
  const mlKindMap = { true: "regression", false: "classification" }
  // after the training the names of the trained models are saved in here
  const [trainedModels, setTrainedModels] = useState()

  // request the available ML models and the respective kind (regression/classification) from the backend
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

  /*
  - delete /download ML files from previous run
  - post /start upload selected ML models and gold label

  TODO: Process the callback, after the training is successfull -> request the performance metrics and display them
  */ 
  const startTraining = () => {
    console.log('selectedModels', selectedModels)
    console.log('goldLabel', goldLabel)
    //start the training if at leased one model is selected and the gold label is set
    if ( !(selectedModels.length === 0) && goldLabel ) {
      var trainingParams = {selectedModels: selectedModels, gold_label: goldLabel}

      // requests to the backend
      //const deletePrevModels = axios.delete(`${backendUrl}/download`)
      const training = axios.post(`${backendUrl}/start`, trainingParams)
      
      // sending both requests 
      // TODO: Comment in again after troubleshooting
      // deletePrevModels.then((cb) => {
      //   console.log('callback of the deletion step', cb)
      //   })
      
      training.then( (response) => {
        try {  
          console.log('cb of the training process', response)
          var availTrainModels = response.data["trained"]
          setTrainedModels(availTrainModels)
        } catch { console.log("Could not retrieve the name of the trained models from the /training endpoint repsonse.")}
      })
    }
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
        <Selector csvColumns={csvColumns} csvRows={csvRows} setGoldLabel={setGoldLabel}/>
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
          <button className="button" onClick={() => startTraining()}>
            <span>Go!</span>
          </button>

          { trainedModels && <ModelDownloader availModels={trainedModels} backendUrl={backendUrl} /> }

        </div>
      </div>
      <div className="cardContainer box4"></div>
    </div>
  );
}

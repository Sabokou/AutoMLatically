import React from 'react'

import axios from "axios";
import { saveAs } from 'file-saver';

import './ModelDownloader.css'

function ModelDownloader({ availModels, backendUrl }) {
    
    const downloadModel = (modelName=undefined) => {
        // if the name is undefined download the best model otherwise download the model by name
        var reqParams
        if (typeof modelName === 'string' || modelName instanceof String) {
          //request model by name
          reqParams = {model: modelName}
        } else {
          //request the top model
          reqParams = {top: true}
        }
         
        // params must be used for get requests. axios doesnt support get with data in the body
        // const bestRequest = axios.get(`${backendUrl}/download`, {params: bestParams})
        // bestRequest.then( (cb) => {
        //   console.log("Downloaded the file", cb);
        // })
    
        // https://stackoverflow.com/questions/41938718/how-to-download-files-using-axios
        axios({
          url: `${backendUrl}/download`,
          method: 'GET',
          responseType: 'blob', // to make sure the model file is recognized by axios
          params: reqParams
        }).then((response) => {
            console.log("Downloaded the file", response);
            var fName = "model.joblib"
            // Try to extract the filename from header. See: https://medium.com/@nerdyman/prompt-a-file-download-with-the-content-disposition-header-using-fetch-and-filesaver-8683faf565d0
            try {
              fName = response.headers['content-disposition'].split(';')
              .find(n => n.includes('filename='))
              .replace('filename=', '')
              .trim();
            } catch { }
            
            // save the file on client with server-side name
            saveAs(response.data, fName)
        });
      }

  return (
    <div>
        <div className='fill downloadTitle'>Download trained models:</div>
        <button className="download fill" onClick={() => downloadModel()}>
            <span>Download Best Model</span>
        </button>
        <div>
            <select id="modelDownloadSelector">
            {availModels.map((item) => {
                return <option value={item}>{item}</option>;
            })}
            </select>
            <button className="download" onClick={() => {
                var select = document.getElementById('modelDownloadSelector')
                var model = select.options[select.selectedIndex].text
                downloadModel(model)
            }}>
                <span>Download</span>
            </button>
        </div>
    </div>
  )
}

export default ModelDownloader
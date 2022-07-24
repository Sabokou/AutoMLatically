import React, { useState } from "react";
import axios from "axios";
import CsvLoader from "./CsvLoader";

export const FileUploader = ({ setCsvColumns, setCsvRows }) => {
  const [file, setFile] = useState();
  const onInputChange = (e) => {
    console.log(e.target.files);
    CsvLoader(e.target.files[0], setCsvColumns, setCsvRows);
    setFile(e.target.files[0]);
  };
  const submit = (e) => {
    e.preventDefault();
    
    console.log('file', file)
    const data = new FormData();
    data.append("file", file);

    // axios library which serves as a middleware
    axios
      .post("//localhost:8001/upload", data)
      .then((e) => {
        console.log("Uploaded the file");
      })
      .catch((e) => {
        console.error("Error", e);
      });
  };
  return (
    // Upload form
    <form className="m-3" method="post" action="#" id="#" onSubmit={submit}>
      <label className="mx-3" style={{color: "white"}}>Choose file: </label>
      <input
        className="form-control"
        type="file"
        onChange={onInputChange}
        multiple=""
        accept=".csv"
      />
      <button className="btn btn-light btn-outline-primary">Upload</button>
    </form>
  );
};

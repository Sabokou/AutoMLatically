import React, { useState } from "react";
import axios from "axios";

export const FileUploader = ({}) => {
  const [file, setFile] = useState(null);
  const onInputChange = (e) => {
    console.log(e.target.files);
    setFile(e.target.files[0]);
  };
  const onSubmit = (e) => {
    e.preventDefault();

    const data = new FormData();
    data.append("file", file);
    
    // axios library which serves as a middleware
    axios
      .post("//localhost:8000/upload", data)
      .then((e) => {
        console.log("Working");
      })
      .catch((e) => {
        console.error("Error", e);
      });
  };
  return (
    // Upload form
    <form className="m-3" method="post" action="#" id="#" onSubmit={onSubmit}>
      <label className="mx-3">Choose file: </label>
      <input
        className="form-control"
        type="file"
        onChange={onInputChange}
        multiple=""
      />
      <button className="btn btn-outline-primary">Upload</button>
    </form>
  );
};

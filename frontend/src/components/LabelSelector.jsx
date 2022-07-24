import React from "react";
import { FileUploader } from "./fileUploader";
import { useState } from "react";
import CsvPreview from "./CsvPreview";

export default function Selector(props) {
  var doColsExist = !(typeof props.csvColumns === 'undefined')

  const onLabelChange = (e) => {
    props.setGoldLabel(e.target.value)
  }

  return (
    <div className="content">
      {/* This code with the column dropdown can be used for the gold label selection in a card */}
      {
        !doColsExist && <div style={{color: "white", justifySelf: "center"}}>Upload a CSV file to see it's labels.</div>
      }
      {
        // Dropdown to select gold-label
          doColsExist && <select onChange={onLabelChange}>
            {props.csvColumns.map((item) => {
              return <option value={item}>{item}</option>;
            })}
          </select>
      }
    </div>
  );
}

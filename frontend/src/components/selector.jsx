import React from "react";
import { FileUploader } from "./fileUploader";
import { useState } from "react";
import CsvPreview from "./CsvPreview";

export default function Selector(props) {
  return (
    <div className="content">
      {/* This code with the column dropdown can be used for the gold label selection in a card */}
      {
        // Dropdown to select gold-label
        props.csvColumns && (
          <select>
            {props.csvColumns.map((item) => {
              return <option value={item}>{item}</option>;
            })}
          </select>
        )
      }
    </div>
  );
}

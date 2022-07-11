import React, { useState } from 'react'

import './ModelSelector.css'

function ModelSelector({ availModels, modelKind, selectedModels, setSelectedModels }) {
    console.log('availModels', availModels)
    console.log('modelKind', modelKind)

    // read the models for the selected type (regression, classification)
    const checkList = availModels[modelKind]

    // Add/Remove item from state
    const handleCheck = (event) => {
        var checkValue = event.target.value
        var updatedList = selectedModels
        
        
        // add the selected model if it isn't already in state
        if (event.target.checked) {
            if ( !(selectedModels.includes(checkValue)) ) { 
                updatedList = [...selectedModels, checkValue];
            }
        // if it is unchecked remove it from the state list
        } else {
            updatedList.splice(selectedModels.indexOf(checkValue), 1);
        }
        console.log('updatedList', updatedList)
        setSelectedModels(updatedList);
    }

    const syncStateCheck = (event) => {
        // check if the checkbox is in state -> return true if it is and should be checked
        var checkboxTitle = event.target.value 
        var isInState = selectedModels.contains(checkboxTitle)
        return isInState
    }

    return (
        <div>
            <div className="check-list">
                <div className="model-selector-title">Select Models for Training:</div>
                <div className="list-container">
                    {checkList.map((item, index) => (
                        <div key={item}>
                            <input value={item} type="checkbox" onChange={handleCheck} defaultChecked={false}/>
                            <span className="model-item-text">{item}</span>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
}

export default ModelSelector

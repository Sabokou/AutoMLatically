import axios from "axios"

export default function RequestModels() {
    const backendUrl = "http://localhost:8001"

    // axios library which serves as a middleware
    // get all available ml models from the backend 
    // if the data is not present already
    var availModels;
    const storageName = "AvailModels"

    // if the localstorage item does not exist
    if (!(localStorage.getItem(storageName))) {
        console.log('localstorage is empty and will be filled')
        axios
            .get(`${backendUrl}/model-names`)
            .then((e) => {
                // if successfull, save the response data to the state or localstorage
                console.log("Received event:", e);
                console.log("The received data is: ", e.data)
                localStorage.setItem(storageName, JSON.stringify(e.data))
                console.log('The localstorage contains this value now:', localStorage.getItem(storageName))
            })
            .catch((e) => {
                console.error("Received error", e);
            });
    } else {
        console.log("The localstorage entry already exists:", JSON.parse(localStorage.getItem(storageName)));
    }

    availModels = JSON.parse(localStorage.getItem(storageName))
    console.log('availModels in requestmodels', availModels)
    //read the models from the localstorage and return them
    return availModels
}

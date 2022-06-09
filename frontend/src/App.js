import './App.css';
import Home from "./pages/homepage";
import { BrowserRouter, Routes, Route} from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import NavbarBar from "./components/navbar";


function App() {
  return (

    <BrowserRouter>
      <NavbarBar/>
      {/* <Sidebar/> */}
      <Routes>
        <Route path="/" exact element={<Home/>} />
      </Routes>
    </BrowserRouter>
  )};
  //   <div className="App">
  //     <header className="App-header">
  //       <img src={logo} className="App-logo" alt="logo" />
  //       <p>
  //         Edit <code>src/App.js</code> and save to reload.
  //       </p>
  //       <a
  //         className="App-link"
  //         href="https://reactjs.org"
  //         target="_blank"
  //         rel="noopener noreferrer"
  //       >
  //         Learn React
  //       </a>
  //     </header>
  //   </div>
  // );


export default App;

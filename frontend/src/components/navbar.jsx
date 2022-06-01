import React from "react";
import Navbar from "react-bootstrap/Navbar";
import NavDropdown from "react-bootstrap/NavDropdown";
import Nav from "react-bootstrap/Nav";
import Container from "react-bootstrap/Container";
import "./navbar.css";


const NavbarBar = (props) => {
  return (

    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
      <a class="navbar-brand" href="#">
        AutoMLatically - The powerful Tool for your Machine Learning Use-Case
      </a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNavDropdown"
        aria-controls="navbarNavDropdown"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse col-md-3" id="navbarNavDropdown">
        <ul class="navbar-nav ">
          <li class="nav-item active">
            <a class="nav-link" href="#">
              Home <span class="sr-only">(current)</span>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">
              Features
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">
              Pricing
            </a>
          </li>
          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle"
              href="#"
              id="navbarDropdownMenuLink"
              data-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="false"
            >
              Dropdown link
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
              <a class="dropdown-item" href="#">
                Action
              </a>
              <a class="dropdown-item" href="#">
                Another action
              </a>
              <a class="dropdown-item" href="#">
                Something else here
              </a>
            </div>
          </li>
        </ul>
      </div>
      <button className="upload">Upload</button>
    </nav>
  );
}

export default NavbarBar;

// const NavbarBar = (props) => {
//     return (
//       <nav className="navbar">
//       <div className="navLogo">
//         <Link to="/" className="fas fa-coffee logoBrown"></Link>
//         <h4 className="header">AutoMLatically</h4>
//       </div>
//       <ul className="navbarUL">
//         <li className="navComponent">
//           <Link to="/" className="navLinks">
//             <h3>Home</h3>
//           </Link>
//         </li>
  
//         <li className="navComponent">
//           <Link to="/produkte" className="navLinks">
//             <h3>Produkte</h3>
//           </Link>
//         </li>
  
//         <li className="navComponent">
//           <Link to="/services" className="navLinks">
//             <h3>Services</h3>
//           </Link>
//         </li>
//       </ul>  </nav>
//     );
//   }
  
//   export default NavbarBar;
  

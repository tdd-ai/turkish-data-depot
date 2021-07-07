import styled from "styled-components";
import Navbar from "react-bootstrap/Navbar";

import Logo from "../assets/TDD-eng-color.png";

const Styles = styled.div`
  .tdd-logo {
    height: 50px;
  }

  .navbar {
    box-shadow: inset 0px -1px 0px #e2e2ea;
    background-color: #fff;
  }
`;

const NavigationBar = () => {
  return (
    <Styles>
      <Navbar expand="lg">
        <img className="tdd-logo" src={Logo} alt="logo" />
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
      </Navbar>
    </Styles>
  );
};

export default NavigationBar;

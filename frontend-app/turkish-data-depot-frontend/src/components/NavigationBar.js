import styled from "styled-components";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import Logo from "../assets/TDD-eng-color.png";

const Styles = styled.div`
  .tdd-logo {
    height: 50px;
  }
`;

const NavigationBar = (props) => {
  return (
    <Styles>
      <Navbar bg="light" expand="lg">
        <img className="tdd-logo" src={Logo} alt="logo" />
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
      </Navbar>
    </Styles>
  );
};

export default NavigationBar;

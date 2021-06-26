import logo from "./logo.svg";
import "./App.css";
import styled from "styled-components";
import NavigationBar from "./components/NavigationBar";
import Datasets from "./screens/Datasets";
import { HashRouter as Switch, Route } from "react-router-dom";

const Styles = styled.div`
  font-family: "Montserrat", -apple-system, BlinkMacSystemFont, "Segoe UI",
    Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji",
    "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
`;

function App() {
  return (
    <Styles>
      <NavigationBar />
      <Switch>
        <Route path="/">
          <Datasets />
        </Route>
      </Switch>
    </Styles>
  );
}

export default App;

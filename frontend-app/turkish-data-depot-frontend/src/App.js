import logo from "./logo.svg";
import "./App.css";
import styled from "styled-components";
import NavigationBar from "./components/NavigationBar";
import Datasets from "./screens/Datasets";
import { BrowserRouter as Switch, Route } from "react-router-dom";

const Styles = styled.div``;

function App() {
  return (
    <Styles>
      <NavigationBar />
      <Switch>
        <Route path="/datasets">
          <Datasets />
        </Route>
      </Switch>
    </Styles>
  );
}

export default App;
